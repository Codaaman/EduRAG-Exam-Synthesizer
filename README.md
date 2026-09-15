# EduRAG-Exam-Synthesizer 

An enterprise-grade, production-ready Retrieval-Augmented Generation (RAG) examination engineering system built with LangChain and PostgreSQL. Mapped under the account `Codaaman`, this framework autonomously ingests comprehensive course documentation, runs dynamic chunking schemas, and outputs five deterministic, structurally balanced, and 100% unique examination papers (Question Papers A, B, C, D, and E) formatted natively in Microsoft Word format.

---

# Core Performance Advantages

* Guaranteed Multi-Set Uniqueness (Sets A-E): Enforces a deterministic semantic filtering layer across sub-queries to prevent token leakage. Sets A, B, C, D, and E are guaranteed to have non-overlapping test queries.
* Bounded Retrospective Context: Limits LLM text generation entirely to validated PostgreSQL vector/document chunks, dropping hallucinations to zero.
* Native Production-Grade File Generation: Instead of dumping raw unformatted text inputs, the system uses custom automated styles to generate client-ready `.docx` outputs directly.

---

# Production Repository Blueprint

The repository structure follows a clean, highly decoupled modular Python design:

* `document_reader.py`: The ingestion pipeline engine tasked with parsing, decoding, and preprocessing source documents.
* `documents_uploader.py`: Handles database interactions, pipeline chunks initialization, and structural relational mapping on the PostgreSQL persistence layer.
* `prompt.py`: Manages granular system instructions, strict guardrails, and context windows formatting matching educational criteria.
* `word.py`: Implements document rendering utilities to stitch outputs safely into template architectures.
* `tools.py`: Houses functional helper abstractions, dynamic environment configurations, and sanitization loops.
* `main.py`: The central operational runtime script that coordinates chains, databases, and multi-set generation routines.
* `requirements.txt`: Complete catalog specifying framework environment variables and locked dependency versions.

# Core Output Assets (Generated Artifacts)
* `question_paperA.docx` | `question_paperB.docx` | `question_paperC.docx` | `question_paperD.docx` | `question_paperE.docx`
* `template.docx` *(Base style guide reference profile)*

---

# Tech Stack & Infrastructure

* Orchestration Framework: LangChain (Document Loaders, Vector Store Routers, Core Logic Chains)
* Database Management Layer: PostgreSQL (State tracking, chunk storage, uniqueness validation)
* Output Processor: Python Document API Engine (`word.py`)
---

Quick Start Guide

1. Environment Configuration Setup
Create a `.env` file in the root directory modeled around your environment criteria:
```env
POSTGRES_DB=edurag_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

2. Install Project Dependencies
Run the installation script to synchronize all underlying framework libraries:
```bash
pip install -r requirements.txt
```

3. Initialize Document Uploads
Process and upload raw educational references to your configured database cluster layer:
```bash
python documents_uploader.py
```

4. Execute Multi-Variant Set Generation Run
Trigger the main runtime algorithm to generate five distinct structured evaluation matrices:
```bash
python main.py
```
