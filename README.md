##InformoAI 💬##
InformoAI is a Retrieval-Augmented Generation (RAG) based chatbot that answers questions using the contents of uploaded documents (PDF or DOCX). It supports multiple documents, saving embeddings for each one, and can still provide answers using general knowledge if no relevant information is found in the documents.

##FEATURES##
Document Upload: Users can upload PDF or DOCX files containing information.
Text Extraction & Chunking: The app extracts text from the uploaded file, splits it into manageable chunks for efficient retrieval.
Semantic Search: The app uses the FAISS vector store and OpenAI embeddings to find the most relevant chunks of text for the user's query.
General Knowledge Querying: If no relevant text is found, the app uses OpenAI’s GPT to provide an answer based on general knowledge.
User Interaction: Simple and intuitive interface for users to ask questions related to the content of their uploaded files.
