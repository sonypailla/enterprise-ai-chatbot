# Enterprise AI Chatbot (Agentic RAG System)

## Overview
This project is a simple enterprise AI chatbot designed to answer user questions using internal documents instead of relying only on the language model. It demonstrates an agentic Retrieval-Augmented Generation (RAG) workflow suitable for enterprise knowledge use cases.

## Problem
Enterprises often store knowledge across documents that are difficult to search using traditional keyword-based systems. This chatbot allows users to ask natural-language questions and receive accurate, context-aware answers grounded in internal data.

## Architecture
- **LLM:** OpenAI GPT (via API)
- **Agent Framework:** LangChain
- **Vector Database:** ChromaDB (local)
- **Backend:** FastAPI
- **Language:** Python

Documents are ingested, chunked, embedded, and stored in a vector database. When a user submits a query, the system retrieves relevant document chunks and passes them to the LLM to generate grounded responses.

## Agent Behavior
The chatbot first determines whether retrieval is required. If so, it performs semantic search over stored embeddings and constructs a context-aware prompt. This retrieval-first approach helps reduce hallucinations and improves factual accuracy.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Set your OpenAI API key as an environment variable
3. Run `python ingest.py`
4. Start the API: `uvicorn app:app --reload`
5. Query the chatbot at `/chat?query=your_question`

## Notes
This project focuses on clarity, correctness, and explainability rather than UI complexity. It demonstrates core skills required for building enterprise AI chatbot and agent systems.

