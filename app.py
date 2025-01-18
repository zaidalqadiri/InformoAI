import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from docx import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

def main():
    st.header("InformoAI💬")

    load_dotenv()

    uploaded_file = st.file_uploader("Upload your file", type=['pdf', 'docx'])
    vectorStore = None

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1].lower()
        text = ''

        # Handle PDF files
        if file_extension == 'pdf':
            pdf_reader = PdfReader(uploaded_file)

            for page in pdf_reader.pages:
                text += page.extract_text()
        
         # Handle DOCX files
        elif file_extension == 'docx':
            doc = Document(uploaded_file)
            for paragraph in doc.paragraphs:
                text += paragraph.text + '\n'

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        # Divide data into chunks
        chunks = text_splitter.split_text(text=text)
        
        store_name = uploaded_file.name.split('.')[0]  # remove the file formats

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
            st.success(f"Embeddings saved successfully")

    # User question
    query = st.text_input(f"Ask questions about your file...")
    st.write(f"You: {query}")

    if query:
        if vectorStore is None:
            st.error("Please upload a file")
        else:
            # Semantic search to find chunks most similar to the query
            docs = vectorStore.similarity_search(query=query, k=3)
            
            # Initialize LLM and run the chain
            llm = OpenAI()
            chain = load_qa_chain(llm=llm, chain_type='stuff')
            response = chain.run(input_documents=docs, question=query)
            st.write(f"InformoAI: {response}")

if __name__ == '__main__':
    main()