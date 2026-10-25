
import os
from dotenv import load_dotenv
import streamlit as st

from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()



# Page configuration
st.set_page_config(
    page_title="AI Medical Chatbot",
    page_icon="🩺",
    layout="centered"
)

DB_FAISS_PATH = "vectorstore/db_faiss"

CUSTOM_PROMPT_TEMPLATE = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context

Context: {context}
Question: {question}

Start the answer directly. No small talk please.
"""


# Load FAISS vector database
@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )


# Load Groq LLM
def load_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Set it in .env or environment."
        )

    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.5,
        max_tokens=512,
        groq_api_key=api_key
    )


# Create RAG chain
def get_qa_chain():
    vectorstore = get_vectorstore()

    prompt = PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=load_llm(),
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )


# Streamlit application
def main():

    st.title("🩺 AI Medical Chatbot")
    st.write("Ask questions based on your medical documents.")

    st.warning(
        "This chatbot provides document-based information "
        "and does not replace professional medical advice."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message.get("sources"):
                with st.expander("View source documents"):
                    for i, doc in enumerate(message["sources"], 1):
                        st.markdown(f"**Source {i}**")
                        st.write(doc.metadata)
                        st.write(doc.page_content)

    # Chat input
    user_query = st.chat_input(
        "Ask your medical question..."
    )

    if user_query:

        with st.chat_message("user"):
            st.markdown(user_query)

        st.session_state.messages.append({
            "role": "user",
            "content": user_query
        })

        with st.chat_message("assistant"):
            try:
                with st.spinner("Searching medical documents..."):

                    qa_chain = get_qa_chain()
                    response = qa_chain.invoke({
                        "query": user_query
                    })

                    answer = response["result"]
                    sources = response["source_documents"]

                st.markdown(answer)

                with st.expander("View source documents"):
                    for i, doc in enumerate(sources, 1):
                        st.markdown(f"**Source {i}**")
                        st.write(doc.metadata)
                        st.write(doc.page_content)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
