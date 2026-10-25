# 🩺 AI Medical Chatbot — RAG-Based Question Answering System

An AI-powered medical chatbot that answers user questions based on medical documents using **Retrieval-Augmented Generation (RAG)**. The application retrieves relevant information from a FAISS vector database and uses a Groq-hosted Large Language Model (LLM) to generate context-based answers.

Built with Python, Streamlit, LangChain, Hugging Face embeddings, FAISS, and Groq.

## 🚀 Features

- **Document-Based Question Answering:** Answers questions using information retrieved from your medical knowledge base.
- **Retrieval-Augmented Generation (RAG):** Combines document retrieval with LLM-based response generation.
- **Semantic Search:** Uses Hugging Face sentence embeddings to retrieve relevant document content.
- **FAISS Vector Database:** Efficient similarity search over stored document embeddings.
- **Groq LLM Integration:** Generates answers using the `openai/gpt-oss-120b` model through Groq.
- **Interactive Chat Interface:** Provides a conversational interface built with Streamlit.
- **Chat History:** Maintains previous user questions and assistant responses during the session.
- **Source Documents:** Allows users to inspect the retrieved document content and metadata.
- **Environment Variable Support:** Keeps API credentials outside the source code using `.env`.
- **Medical Safety Notice:** Reminds users that the chatbot does not replace professional medical advice.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and chat interface |
| LangChain | RAG pipeline and prompt management |
| Groq | LLM inference |
| Hugging Face | Text embedding generation |
| Sentence Transformers | Semantic text embeddings |
| FAISS | Vector storage and similarity search |
| python-dotenv | Environment variable management |

## 🧠 How It Works

The application follows a Retrieval-Augmented Generation workflow.

1. **User Question:** The user submits a medical question through the Streamlit chat interface.
2. **Query Retrieval:** The question is used to search the FAISS vector database.
3. **Similarity Search:** The retriever selects the three most relevant document chunks (`k=3`).
4. **Context Preparation:** The retrieved content is passed to the LLM as context.
5. **Answer Generation:** Groq's LLM generates an answer based on the retrieved information and custom prompt.
6. **Source Display:** The application displays the generated answer and provides access to the retrieved source documents.

### Architecture

```text
             User
              |
              v
      Streamlit Chat UI
              |
              v
       User's Question
              |
              v
       LangChain Retriever
              |
              v
       FAISS Vector Store
              |
              v
   Top 3 Relevant Documents
              |
              v
     Custom Prompt Template
              |
              v
       Groq LLM (GPT-OSS)
              |
              v
       Generated Answer
              |
              v
     Answer + Source Documents
```

## 📂 Project Structure

```text
AI-Medical-Chatbot/
│
├── vectorstore/
│   └── db_faiss/
│       ├── index.faiss
│       └── index.pkl
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: The structure above is an example. Adjust the filenames to match your actual project. The FAISS files must be generated or provided before running the application.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rajhandibag/AI-Medical-Chatbot.git
cd AI-Medical-Chatbot
```

Replace the repository URL if your GitHub repository uses a different name.

### 2. Create a virtual environment

Using Python:

```bash
python -m venv medical-chatbot
```

Activate it on Windows PowerShell:

```powershell
.\medical-chatbot\Scripts\Activate.ps1
```

If you are using an existing Conda environment, activate that environment instead.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Ensure that your `requirements.txt` includes the packages required by your code, including:

```text
streamlit
python-dotenv
langchain-groq
langchain-classic
langchain-core
langchain-huggingface
langchain-community
sentence-transformers
faiss-cpu
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Obtain an API key from the [Groq Console](https://console.groq.com/).

**Security:** Never upload your actual API key to GitHub.

### 5. Prepare the FAISS vector database

The application expects the vector database at:

```text
vectorstore/db_faiss/
```

The database must be created from your medical documents using the same compatible embedding model:

```python
sentence-transformers/all-MiniLM-L6-v2
```

Ensure the FAISS index and its associated metadata file are available before starting the application.

### 6. Run the application

```bash
streamlit run app.py
```

Streamlit will display a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser to interact with the chatbot.

## 💬 Example Usage

**Example question:**

> What are the common symptoms of diabetes?

The chatbot searches the indexed medical documents, retrieves relevant passages, and generates an answer based on the available context.

The retrieved source documents can be expanded in the interface to inspect the supporting content.

*The quality and completeness of answers depend on the medical documents indexed in the vector database.*

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to access the Groq LLM |

Keep `.env` out of version control. Add the following entries to `.gitignore`:

```gitignore
.env
.venv/
venv/
__pycache__/
*.py[cod]
```

Do not commit API keys, private medical records, or other sensitive information.

## ⚠️ Important Disclaimer

This project is intended for educational and informational purposes only.

- It is not a substitute for professional medical diagnosis, treatment, or advice.
- Responses depend on the contents and quality of the indexed documents.
- The chatbot may produce incomplete or incorrect answers.
- Always consult a qualified healthcare professional for medical concerns.
- Do not use this application for emergency medical decisions.

## 🔮 Future Improvements

- Support uploading medical PDFs directly through the interface.
- Add document ingestion and vector database creation scripts.
- Improve document chunking and retrieval quality.
- Display source filenames and page numbers alongside answers.
- Add conversation memory and chat history persistence.
- Introduce evaluation metrics for retrieval relevance and answer quality.
- Deploy the application using Streamlit Community Cloud or another hosting platform.
- Add automated tests and a CI/CD workflow.

## 👨‍💻 Author

**Raj Handibag**

- GitHub: [@rajhandibag](https://github.com/rajhandibag)
- LinkedIn: [raj-handibag](https://www.linkedin.com/in/raj-handibag/)

## 📄 License

This project is available for educational use. Add a `LICENSE` file to the repository if you want to specify formal reuse and distribution terms.
