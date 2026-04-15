<<<<<<< HEAD
﻿# RAG Pharma Support System

A starter Python project for building a pharma-focused support assistant with Retrieval-Augmented Generation (RAG).

## Current Project Structure

```text
rag-pharma-support-system/
|- app.py
|- config.py
|- requirements.txt
|- .env
|- README.md
|- data/
|- src/
|  |- loader.py
|  |- chunking.py
|  |- vector_store.py
|  |- rag_pipelines.py
|  |- memory.py
|  |- ticketing.py
|  |- prompts.py
|- venv/
```

## What Was Set Up

1. Created project folder and virtual environment.
2. Created `data/` and `src/` directories.
3. Added starter files (`app.py`, `config.py`, module files in `src/`).
4. Installed dependencies from `requirements.txt`.
5. Configured `.env` for API key loading with `python-dotenv`.
6. Ran `app.py` and validated OpenAI client response.

## Requirements

- Python 3.12+
- PowerShell (Windows)
- OpenAI API key with active quota/billing

## Installation (PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables

Create `.env` in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Important:

- Use `OPENAI_API_KEY` (with underscores), not `OPEN-AI-API-KEY`.
- Keep `.env` in UTF-8 encoding.

## Run

```powershell
python app.py
```

Expected output example:

```text
Hello! Thank you for contacting support. How can I assist you today?
```

## Known Issues and Fixes

### 1) PowerShell `mkdir data src` failed
Use:

```powershell
mkdir data, src
```

### 2) `touch` command not found on Windows
Use:

```powershell
New-Item app.py, requirements.txt, config.py, README.md
```

### 3) Python syntax errors for API key variable names
Invalid in Python:

- `OPEN-AI-API-KEY`

Valid in Python:

- `OPENAI_API_KEY`

### 4) `.env` UnicodeDecodeError (`0xff ... invalid start byte`)
The `.env` file had wrong encoding/BOM. Re-save as UTF-8.

### 5) `OpenAIError: api_key must be set`
Usually caused by one of these:

- Wrong env var name (must be `OPENAI_API_KEY`)
- `.env` not loaded from correct path
- `.env` encoding issue

### 6) `RateLimitError: insufficient_quota`
Your API key worked, but billing/quota was exhausted. After quota became available, request succeeded.

## Security Note

The API key was exposed in terminal history during setup. Rotate/revoke that key in the OpenAI dashboard and replace it with a new key in `.env`.

## Next Development Steps

1. Implement document loading in `src/loader.py`.
2. Add chunking logic in `src/chunking.py`.
3. Build embeddings + FAISS indexing in `src/vector_store.py`.
4. Connect retrieval + response generation in `src/rag_pipelines.py`.
5. Add Streamlit UI after pipeline works in CLI.
=======
# RAG-Capstone-Project
>>>>>>> 1c0b2dd9669ca016cb85c79b063601f22f87593a
