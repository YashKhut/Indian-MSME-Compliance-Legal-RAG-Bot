"""
FastAPI backend — API endpoints for the RAG bot.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.rag.chain import query_rag
from app.rag.ingestion import ingest_text, ingest_pdf
from app.seed_data import SEED_DOCUMENTS

# ─── App ─────────────────────────────────────────────────────
app = FastAPI(
    title="Indian MSME Compliance Bot API",
    description="RAG-powered compliance assistant for Indian MSMEs",
    version="1.0.0",
)

# CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Models ──────────────────────────────────────────────────
class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[dict]


class IngestTextRequest(BaseModel):
    text: str
    metadata: dict = {}


class IngestResponse(BaseModel):
    message: str
    chunks_ingested: int


# ─── Endpoints ───────────────────────────────────────────────
@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "MSME Compliance Bot"}


@app.post("/api/query", response_model=QueryResponse)
def query(request: QueryRequest):
    """Query the RAG system with a compliance question."""
    try:
        result = query_rag(request.question)
        return QueryResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ingest/text", response_model=IngestResponse)
def ingest_text_endpoint(request: IngestTextRequest):
    """Ingest raw text into the knowledge base."""
    try:
        count = ingest_text(request.text, request.metadata)
        return IngestResponse(
            message=f"Successfully ingested text into {count} chunks",
            chunks_ingested=count,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ingest/pdf", response_model=IngestResponse)
async def ingest_pdf_endpoint(file: UploadFile = File(...)):
    """Upload and ingest a PDF document."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    try:
        contents = await file.read()
        count = ingest_pdf(contents, file.filename)
        return IngestResponse(
            message=f"Successfully ingested '{file.filename}' into {count} chunks",
            chunks_ingested=count,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/seed", response_model=IngestResponse)
def seed_knowledge_base():
    """Seed the knowledge base with curated Indian MSME compliance data."""
    try:
        total_chunks = 0
        for doc in SEED_DOCUMENTS:
            count = ingest_text(doc["content"], doc["metadata"])
            total_chunks += count

        return IngestResponse(
            message=f"Successfully seeded knowledge base with {len(SEED_DOCUMENTS)} documents ({total_chunks} chunks)",
            chunks_ingested=total_chunks,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
