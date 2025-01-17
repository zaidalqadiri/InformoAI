import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def main():
    st.header("InformoAI💬")

    pdf = st.file_uploader("Upload your pdf", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text=''

        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        # Divide data into chunks
        chunks = text_splitter.split_text(text=text)

if __name__ == '__main__':
    main()