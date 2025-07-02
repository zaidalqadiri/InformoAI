# InformoAI💬
InformoAI is a Retrieval-Augmented Generation (RAG) based chatbot that answers questions using the contents of uploaded documents.

## Features
* Document Upload: Users can upload PDF or DOCX files containing information.
* Text Extraction & Chunking: The app extracts text from the uploaded file, splits it into manageable chunks for efficient retrieval.
* Semantic Search: The app uses the FAISS vector store and OpenAI embeddings to find the most relevant chunks of text for the user's query.
* General Knowledge Querying: If no relevant text is found, the app uses OpenAI’s GPT to provide an answer based on general knowledge.
* User Interaction: Simple and intuitive interface for users to ask questions related to the content of their uploaded files.

## Screenshots
### Main Page
![Home Page](images/Screenshot%202025-01-22%20222319.png)

### Uploading Document
![Uploading Document](images/Screenshot%202025-01-22%20231049.png)

### Asking Questions and Answer Display
![Asking questions](images/Screenshot%202025-01-22%20224008.png)
![Answer](images/Screenshot%202025-01-22%20230353.png)

## Usage 
1. Upload a Document: Click on the "Upload your file" button to upload a PDF or DOCX file.
2. Ask Questions: Type your questions in the text input box. The chatbot will provide answers based on the content of the uploaded file.
3. View Results: The app will display the answer provided by InformoAI.

## Requirements
1. Python 3.8+
2. Required Python Libraries:
* streamlit - For building the web app interface.
* python-dotenv - To load environment variables (like API keys).
* PyPDF2 - To handle PDF file extraction.
* python-docx - To handle DOCX file extraction.
* langchain - For text splitting, embeddings, and question-answering chains.
* faiss-cpu - For vector store management.

You can install all the dependencies by running the following command:
```bash 
pip install -r requirements.txt
```

## How to Run
### Step 1: Clone the Repository
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/zaidalqadiri/informoai.git
cd informoai
```

### Step 2: Install Dependencies
Navigate to the project directory and install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up OpenAI API Key
Make sure you have an OpenAI API key. You can obtain one by signing up on [OpenAI's website](https://openai.com/).
Once you have the API key, create a .env file in the root directory of the project and add the following:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 4: Run the App
To start the app, run the following command:
```bash
streamlit run app.py
```
This will launch a local web server, and you can view the app in your browser at http://localhost:8501.

## Notes:
* The .env file should be correctly set up with your API key for smooth functioning.
