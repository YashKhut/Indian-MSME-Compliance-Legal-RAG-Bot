"""
Retriever module — performs vector similarity search against Supabase.
"""

from supabase import create_client

from app.config import SUPABASE_URL, SUPABASE_KEY, MATCH_THRESHOLD, MATCH_COUNT
from app.rag.embeddings import generate_query_embedding

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def retrieve(question: str) -> list[dict]:
    """
    Embed the question and perform cosine similarity search
    against the Supabase documents table.

    Returns a list of matching documents with content, metadata, and similarity score.
    """
    # Generate query embedding (optimized for retrieval)
    query_embedding = generate_query_embedding(question)

    # Call the match_documents_v4 RPC function
    response = supabase.rpc(
        "match_documents_v4",
        {
            "query_embedding": query_embedding,
            "match_threshold": MATCH_THRESHOLD,
            "match_count": MATCH_COUNT,
        },
    ).execute()

    results = response.data if response.data else []

    return [
        {
            "id": doc["id"],
            "content": doc["content"],
            "metadata": doc.get("metadata", {}),
            "similarity": round(doc["similarity"], 4),
        }
        for doc in results
    ]
