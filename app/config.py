"""
Configuration module — loads environment variables and initializes clients.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ─── Supabase ───────────────────────────────────────────────
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# ─── Google Gemini ──────────────────────────────────────────
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# ─── RAG Settings ───────────────────────────────────────────
CHUNK_SIZE = 500          # characters per chunk
CHUNK_OVERLAP = 50        # overlap between chunks
MATCH_THRESHOLD = 0.5     # cosine similarity threshold
MATCH_COUNT = 5           # top-K results to retrieve
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "gemini-2.5-flash"
