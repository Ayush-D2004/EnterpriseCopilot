# 🚀 Enterprise Copilot

**Your AI-powered business assistant for internal documentation.**

Enterprise Copilot is a RAG application designed to help enterprises search and interact with their internal knowledge base. Whether it's HR policies, engineering guidelines, or financial reports, Enterprise Copilot provides accurate, source-backed answers to natural language questions.

This project offers two implementations:
1.  **Web Application**: A feature-rich Streamlit interface with voice support, dashboards, and file management.
2.  **CLI**: A lightweight command-line interface for quick, terminal-based interactions.

**Link to Streamlit app** : https://enterprisecopilot.streamlit.app/
---

## ✨ Features

### 🌐 Web Application
-   **Modern UI**: Premium, responsive design with light/dark themes and smooth animations.
-   **Document Management**: Drag-and-drop upload for PDF, DOCX, and TXT files.
-   **Voice-to-Text**: integrated Voice recording and transcription using **AssemblyAI** - ask questions verbally!
-   **Dashboard**: Real-time analytics on document processing and interaction stats.
-   **RAG Engine**: Powered by **Google Gemini** and **LangChain** for high-quality reasoning.
-   **Source Citations**: Answers include references to the specific documents used.

### 💻 CLI Implementation
-   **Fast & Lightweight**: Run queries directly from your terminal.
-   **Focus Mode**: purely text-based helper without UI overhead.
-   **Detailed Logging**: tracks pipeline execution and errors.
-   **Source Citations**: Prints source document names and page numbers for transparency.

---

## 🛠️ Tech Stack

*   **LLM**: Google Gemini (via `langchain-google-genai`)
*   **Embeddings**: HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`)
*   **Vector Query**: FAISS (Facebook AI Similarity Search)
*   **Orchestration**: LangChain
*   **Web Framework**: Streamlit
*   **Audio Transcription**: AssemblyAI

---

## 🚀 Getting Started

### 1. Prerequisites
-   Python 3.8+ installed.
-   API Keys for **Google Gemini**, **HuggingFace**, and **AssemblyAI**.

### 2. Installation

Clone the repository and navigate to the project folder:

```bash
git clone <repository-url>
cd EnterpriseCopilot
```

Create and activate a virtual environment:

```bash
# Windows
python -m venv ECenv
ECenv\Scripts\activate

# Mac/Linux
python3 -m venv ECenv 
source ECenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory and add your API keys:

```ini
GEMINI_API_KEY='your_gemini_api_key'
HUGGINGFACEHUB_API_TOKEN='your_huggingface_token'
ASSEMBLY_AI_API='your_assemblyai_api_key'
```

---

## 💡 Usage

### Running the Web App

Start the Streamlit interface:

```bash
streamlit run webapp/app.py
```

1.  Open your browser (usually `http://localhost:8501`).
2.  Use the **Sidebar** to upload your documents.
3.  Wait for processing (Toast notification will appear).
4.  Go to the **Assistant** tab.
5.  Type or **Record** your question to get answers based on your data!

### Running the CLI

Start the command-line chat:

```bash
python app/main.py
```

1.  Ensure you have processed documents (the CLI implementation expects an index to exist, or you can run `python app/ingest.py` separately if implemented).
2.  Type your query when prompted `🧑 You:`.
3.  View the AI response and sources directly in the terminal.

---