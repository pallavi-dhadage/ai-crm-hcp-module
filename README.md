markdown
# 🤖 AI‑First CRM – HCP Module

> A full‑stack, AI‑driven CRM system for life sciences field representatives to log and manage **Healthcare Professional (HCP)** interactions.  
> Built for a technical assessment, this project demonstrates how **LangGraph**, **Groq LLMs**, and a **dual‑mode interface** (form + chat) can streamline field data entry.

[![React](https://img.shields.io/badge/React-18-blue?logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2-purple)](https://langchain-ai.github.io/langgraph/)
[![Groq](https://img.shields.io/badge/Groq-gemma2--9b--it-orange)](https://console.groq.com/)

---

## 📖 Table of Contents

- [Why This Project?](#why-this-project)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Architecture](#architecture)
- [Setup & Running](#setup--running)
- [Usage](#usage)
- [Assessment Experience](#assessment-experience)
- [Screenshots](#screenshots)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## ❓ Why This Project?

Companies increasingly use **take‑home technical assessments** to evaluate candidates for senior engineering roles. This repository is my submission for a Round‑1 assignment with the following core requirements:

- **Design the “Log Interaction Screen”** – the core of an HCP module.
- Offer **two interaction modes**: a structured form and a conversational chat.
- Build a **LangGraph agent** with at least five tools (two mandatory: `log_interaction` and `edit_interaction`).
- Integrate **Groq’s `gemma2-9b-it`** model for summarisation and entity extraction.
- Use **React + Redux** for the frontend and **FastAPI** for the backend.

This project goes beyond the basic spec by implementing **real‑time streaming**, **Redux state management**, and **AI‑powered entity extraction**, demonstrating both architectural thinking and practical AI integration.

---

## 🧰 Tech Stack

| Layer          | Technology                                                                 |
|----------------|----------------------------------------------------------------------------|
| **Frontend**   | React 18, TypeScript, Redux Toolkit, CSS (Google Inter font)               |
| **Backend**    | Python 3.12, FastAPI, SQLAlchemy, SQLite (pluggable)                      |
| **AI Agent**   | LangGraph, LangChain, Groq (`gemma2-9b-it`)                                |
| **State Mgmt** | Redux (UI, interactions, agent messages)                                   |
| **Comm.**      | REST APIs + Server‑Sent Events (SSE) for streaming chat                   |
| **Database**   | SQLite (easily switch to PostgreSQL/MySQL)                                |
| **Tools**      | 5 custom tools: `log_interaction`, `edit_interaction`, `get_hcp_profile`, `schedule_follow_up`, `analyze_hcp_engagement` |

---

## 🌟 Features

- ✅ **Dual‑mode logging** – use a traditional form or talk to the AI assistant in natural language.
- ✅ **LangGraph ReAct agent** – understands intent, extracts information, and invokes appropriate tools.
- ✅ **AI summarisation** – automatically generates concise, professional summaries from raw notes.
- ✅ **Entity extraction** – pulls out product names, medical topics, and commitments from free text.
- ✅ **Real‑time streaming** – chat responses appear token by token (SSE) for a responsive feel.
- ✅ **State management** – Redux slices keep UI, interaction list, and conversation messages in sync.
- ✅ **Scalable database** – SQLite for development, ready for production with PostgreSQL.
- ✅ **Fully container‑ready** – runs locally with simple commands; can be Dockerised easily.

---

## 🏗️ Architecture
┌─────────────────────┐ ┌──────────────────────────────────────────────────┐
│ React + Redux │ │ FastAPI Backend │
│ ┌───────────────┐ │ REST/ │ ┌──────────────────────────────────────────┐ │
│ │ Form Mode │ │◄─────────┤ │ LangGraph ReAct Agent │ │
│ │ (controlled) │ │ SSE │ │ ┌───────────┐ ┌───────────┐ │ │
│ └───────────────┘ │ │ │ │ Tool 1 │ │ Tool 2 │ ... │ │
│ ┌───────────────┐ │ │ │ │ log_inter.│ │ edit_inter│ │ │
│ │ Chat Mode │ │ │ │ └───────────┘ └───────────┘ │ │
│ │ (SSE stream) │ │ │ └──────────────────────────────────────────┘ │
│ └───────────────┘ │ │ │ │
└─────────────────────┘ │ ▼ │
│ ┌──────────────────────────────────────────┐ │
│ │ Groq LLM (gemma2-9b-it) │ │
│ │ - Summarisation │ │
│ │ - Entity extraction │ │
│ └──────────────────────────────────────────┘ │
│ │ │
│ ┌──────────────────▼───────────────────────┐ │
│ │ SQLite / PostgreSQL (HCP, Interactions) │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────────┘

text

---

## 🚀 Setup & Running

### Prerequisites

- **Python** 3.12+  
- **Node.js** 18+  
- **Groq API Key** – obtain free from [console.groq.com](https://console.groq.com)

---

### Backend

```bash
# Clone the repository
git clone https://github.com/pallavi-dhadage/ai-crm-hcp-module.git
cd ai-crm-hcp-module/backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env   # Add your GROQ_API_KEY and other settings

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
The server will be available at http://localhost:8000.
API documentation is automatically generated at /docs.

Frontend
bash
cd ../frontend

# Install dependencies
npm install

# Start the development server
npm start
The frontend will run at http://localhost:3000.

Testing the Agent
Open the frontend, switch to Chat mode, and send a message like:

text
Log a meeting with Dr. Smith on 2026-07-10. We discussed the new drug X. He was positive about the results.
The agent will:

Parse the request.

Call log_interaction with extracted data.

Generate an AI summary.

Return a confirmation.

💼 Assessment Experience
What the Assignment Required
Build the “Log Interaction Screen” with both a form and a chat interface.

Implement a LangGraph agent with at least 5 tools (two mandatory: log_interaction, edit_interaction).

Use Groq’s gemma2-9b-it for AI capabilities.

Follow a React + Redux / FastAPI stack.

What I Delivered (Beyond the Spec)
Real‑time streaming – the chat interface shows responses token by token (SSE), improving UX.

Professional summarisation – the LLM not only extracts data but also writes a polished summary.

Entity extraction – products, topics, and commitments are automatically pulled from notes.

Clean state management – Redux slices keep the UI in sync with the data layer.

Comprehensive error handling – graceful fallbacks and clear error messages.

Challenges & Learnings
LangGraph State Schema – Initially struggled to extend the AgentState correctly. Solved by subclassing MessagesState to include custom fields like current_interaction_id.

CORS and SSE – Configured FastAPI to accept localhost:3000 and set the correct media_type for event streaming.

Frontend Caching – The browser stubbornly served old versions; learned to clear node_modules/.cache and use incognito windows for testing.

Submodule Pitfall – Accidentally committed the frontend folder as a submodule; fixed by removing .git inside it and re‑adding normally.

Time Spent
Core functionality (agent, tools, endpoints): ~6 hours

Frontend UI & Redux integration: ~3 hours

Polishing, README, and deployment: ~2 hours

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

🙌 Acknowledgements
LangChain & LangGraph – for the agent framework.

Groq – for providing fast, free LLM inference.

FastAPI – for the elegant backend framework.

React & Redux Toolkit – for frontend development.

📬 Contact
If you have any questions or feedback, feel free to open an issue or reach out directly.

Happy building! 🚀
