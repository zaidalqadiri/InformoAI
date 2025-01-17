import streamlit as st
import pickle
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def main():
    st.header("InformoAI💬")

    # load_dotenv()

    pdf = st.file_uploader("Upload your pdf", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''

        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        # Divide data into chunks
        chunks = text_splitter.split_text(text=text)
        
        store_name = pdf.name[:-4]  # remove the file formats

        # Check if FAISS index exists
        if os.path.exists(f"{store_name}.faiss") and os.path.exists(f"{store_name}.json"):
            # Load the FAISS vector store
            vectorStore = FAISS.load_local(store_name, OpenAIEmbeddings())
            st.success(f"Embeddings loaded successfully")
        else:
            # Generate embeddings
            embeddings = OpenAIEmbeddings() 
            vectorStore = FAISS.from_texts(chunks, embedding=embeddings)

            # Save the FAISS vector store
            vectorStore.save_local(store_name)
            st.success(f"Embeddings stored successfully")

if __name__ == '__main__':
    main()