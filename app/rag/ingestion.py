"""
Document ingestion module — chunks text, generates embeddings, stores in Supabase.
"""

import io
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from supabase import create_client

from app.config import (
    SUPABASE_URL,
    SUPABASE_KEY,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)
from app.rag.embeddings import generate_embedding, generate_embeddings_batch

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=len,
    separators=["\n\n", "\n", ". ", ", ", " ", ""],
)


def ingest_text(text: str, metadata: dict | None = None) -> int:
    """
    Chunk text, generate embeddings in batch, and store in Supabase.
    Returns the number of chunks ingested.
    """
    if metadata is None:
        metadata = {}

    chunks = text_splitter.split_text(text)
    if not chunks:
        return 0

    # Batch generate embeddings for all chunks in one call
    try:
        embeddings = generate_embeddings_batch(chunks)
    except Exception as e:
        # Fallback to individual calls if batch fails (or for debugging)
        print(f"Batch embedding failed: {e}. Falling back to individual calls.")
        embeddings = [generate_embedding(chunk) for chunk in chunks]

    records = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        chunk_metadata = {
            **metadata,
            "chunk_index": i,
            "total_chunks": len(chunks),
        }
        records.append({
            "content": chunk,
            "metadata": chunk_metadata,
            "embedding": embedding,
        })

    # Batch insert into Supabase
    if records:
        supabase.table("documents").insert(records).execute()

    return len(records)


def ingest_pdf(file_bytes: bytes, filename: str = "uploaded.pdf") -> int:
    """
    Extract text from a PDF, then ingest it.
    Returns the number of chunks ingested.
    """
    reader = PdfReader(io.BytesIO(file_bytes))
    full_text = ""

    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            full_text += f"\n\n--- Page {page_num + 1} ---\n\n{page_text}"

    metadata = {
        "source": filename,
        "type": "pdf",
        "total_pages": len(reader.pages),
    }

    return ingest_text(full_text, metadata)
