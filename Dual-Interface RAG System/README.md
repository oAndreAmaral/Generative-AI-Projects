# Dual-Interface RAG System

**Project created by André Amaral in 2026**  

A desktop and web-based **Retrieval-Augmented Generation (RAG) system** that allows users to provide context documents (PDFs) and analyze target documents to generate detailed reports. Supports **dual interfaces**: **Tkinter GUI** for desktop and **Streamlit** for web.

---

## Features

- **Contextual Analysis:** Upload multiple PDFs as context to build a vector database.  
- **RAG Techniques:**
  - **Simple RAG:** Analyze a target document and generate a detailed report highlighting errors, points of attention, and suggestions.  
- **Dual Interface:**  
  - **Tkinter:** Desktop application with PDF report output (application.py).  
  - **Streamlit:** Web interface for RAG queries chatbot (chatbot.py).  
- **Vector Database Persistence:**
  - **Chroma** to store embeddings incrementally (append new context documents without overwriting old ones).  
- **LLM Integration:**
  - **ChatGroq API** for fast, accurate LLM responses.  
- **Embeddings:** Supports HuggingFaceEmbeddings embeddings (**OpenAI Embeddings**) for compatibility and speed.

---

## System Requirements

- **Python 3.11 64-bit** (32-bit Python supported for other projects, but Chroma + embeddings require 64-bit)  
- Internet connection for API calls (ChatGroq)  
- Required Python packages listed in `requirements.txt`  

---

## Installation

1. **Clone or download this repository**  

2. **Create a virtual environment (64bits)**  

py -3.11 -m venv venv_ai_rag

3. **Activate the virtual environment**  

venv_ai_rag\Scripts\activate

4. **Install dependencies**  

python.exe -m pip install --upgrade pip

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

pip install -r requirements.txt

5. **Create and update the .venv according to the env_template.txt**  

---

## Usage

- **Chatbot Mode:** It is a chatbot mode where queries and interactive conversations can be performed

  streamlit run chatbot.py 

- **Application Mode:** It is an application that allows to select context files, the file to analyze and generates a report

  python application.py 


Note: there are some scripts inside the utils folder to help understand the behaviour of the vector database.