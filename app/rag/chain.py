"""
RAG Chain — orchestrates retrieval + Gemini 2.0 Flash answer generation.
"""

import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from app.config import LLM_MODEL
from app.rag.retriever import retrieve

SYSTEM_PROMPT = """You are an expert Indian MSME Compliance Assistant. Your job is to help 
small and medium business owners in India understand compliance requirements, tax exemptions, 
labor laws, GST rules, MSME registration processes, and state-specific incentive policies.

INSTRUCTIONS:
1. Answer ONLY based on the provided context documents. If the context doesn't contain 
   relevant information, say so clearly — do NOT make up information.
2. Provide clear, plain-English summaries that a non-legal business owner can understand.
3. Always cite the source section/document when referencing specific rules or laws.
4. When mentioning monetary thresholds, always include the currency (₹ / INR).
5. If multiple rules or exemptions apply, organize them as a numbered list.
6. Mention any important caveats, deadlines, or conditions that apply.
7. If the question is about a specific state (e.g., Gujarat), prioritize state-specific 
   information alongside central government rules.

CONTEXT DOCUMENTS:
{context}

USER QUESTION: {question}

Provide a comprehensive but concise answer with source citations."""


def query_rag(question: str) -> dict:
    """
    Full RAG pipeline:
    1. Retrieve relevant document chunks from Supabase
    2. Build a prompt with context
    3. Generate answer using Gemini 2.0 Flash
    4. Return answer + sources
    """
    # Step 1: Retrieve relevant chunks
    sources = retrieve(question)

    if not sources:
        return {
            "answer": (
                "I couldn't find relevant information in my knowledge base for your question. "
                "This might be because:\n"
                "- The knowledge base hasn't been seeded yet (click 'Seed Knowledge Base' in the sidebar)\n"
                "- The topic isn't covered in the current documents\n\n"
                "Try seeding the knowledge base first, or upload relevant compliance PDFs."
            ),
            "sources": [],
        }

    # Step 2: Build context from retrieved documents
    context_parts = []
    for i, doc in enumerate(sources, 1):
        source_name = doc["metadata"].get("source", "Unknown")
        category = doc["metadata"].get("category", "General")
        context_parts.append(
            f"[Source {i}] ({source_name} | {category} | Relevance: {doc['similarity']:.0%})\n"
            f"{doc['content']}"
        )
    context = "\n\n---\n\n".join(context_parts)

    # Step 3: Generate answer with Gemini 1.5 Flash
    prompt = SYSTEM_PROMPT.format(context=context, question=question)

    try:
        import google.generativeai as genai
        from app.config import GOOGLE_API_KEY
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel(LLM_MODEL)
        response = model.generate_content(prompt)
        answer = response.text
    except Exception as e:
        answer = f"Error generating answer with Gemini: {str(e)}\n\n(Did you add GOOGLE_API_KEY to .env?)"


    # Step 4: Format sources for display
    formatted_sources = []
    for doc in sources:
        formatted_sources.append({
            "content": doc["content"][:200] + "..." if len(doc["content"]) > 200 else doc["content"],
            "source": doc["metadata"].get("source", "Unknown"),
            "category": doc["metadata"].get("category", "General"),
            "similarity": f"{doc['similarity']:.0%}",
        })

    return {
        "answer": answer,
        "sources": formatted_sources,
    }
