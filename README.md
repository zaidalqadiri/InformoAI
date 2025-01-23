# InformoAI
InformoAI is a Retrieval-Augmented Generation (RAG) based chatbot that answers questions using the contents of uploaded documents.

## FEATURES
* Document Upload: Users can upload PDF or DOCX files containing information.
* Text Extraction & Chunking: The app extracts text from the uploaded file, splits it into manageable chunks for efficient retrieval.
* Semantic Search: The app uses the FAISS vector store and OpenAI embeddings to find the most relevant chunks of text for the user's query.
* General Knowledge Querying: If no relevant text is found, the app uses OpenAI’s GPT to provide an answer based on general knowledge.
* User Interaction: Simple and intuitive interface for users to ask questions related to the content of their uploaded files.

## Requirements
1. Python 3.8+
2. Required Python Libraries:
* streamlit - For building the web app interface.
* python-dotenv - To load environment variables (like API keys).
* PyPDF2 - To handle PDF file extraction.
* python-docx - To handle DOCX file extraction.
* langchain - For text splitting, embeddings, and question-answering chains.
* faiss-cpu - For vector store management.