"""
Embedding module — generates vector embeddings using Google Gemini.
"""

import os
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL

# Initialize the local HuggingFace embedding model
# This downloads the model (~90MB) on the first run and caches it
hf_embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def generate_embedding(text: str) -> list[float]:
    """Generate a 384-dimensional embedding for the given text using HuggingFace."""
    if not text.strip():
        return [0.0] * 384
    return hf_embeddings.embed_query(text)


def generate_embeddings_batch(texts: list[str]) -> list[list[float]]:
    """Generate embeddings for a list of texts in a single batch call."""
    if not texts:
        return []
    
    # Remove empty texts to avoid errors
    valid_texts = [t if t.strip() else " " for t in texts]
    return hf_embeddings.embed_documents(valid_texts)


def generate_query_embedding(text: str) -> list[float]:
    """Generate an embedding optimized for search queries."""
    if not text.strip():
        return [0.0] * 384
    return hf_embeddings.embed_query(text)
