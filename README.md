**InformoAI** 💬
InformoAI is a Retrieval-Augmented Generation (RAG) based chatbot that can answer questions using the contents of a user-uploaded document (PDF or DOCX). If no relevant information is found in the document, it will provide answers using general knowledge powered by OpenAI's GPT model.

Features
Document Upload: Users can upload PDF or DOCX files containing information.
Text Extraction & Chunking: The app extracts text from the uploaded file, splits it into manageable chunks for efficient retrieval.
Semantic Search: The app uses the FAISS vector store and OpenAI embeddings to find the most relevant chunks of text for the user's query.
General Knowledge Querying: If no relevant text is found, the app uses OpenAI’s GPT to provide an answer based on general knowledge.
User Interaction: Simple and intuitive interface for users to ask questions related to the content of their uploaded files.
Requirements
Python 3.8+
Required Python Libraries:
streamlit - For building the web app interface.
python-dotenv - To load environment variables (like API keys).
PyPDF2 - To handle PDF file extraction.
python-docx - To handle DOCX file extraction.
langchain - For text splitting, embeddings, and question-answering chains.
faiss-cpu - For vector store management.
You can install all the dependencies by running the following command:

bash
Copy
Edit
pip install -r requirements.txt
Make sure to have the .env file for your OpenAI API key configuration.
