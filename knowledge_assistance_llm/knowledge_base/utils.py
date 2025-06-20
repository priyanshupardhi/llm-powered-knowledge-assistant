from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from django.conf import settings

def process_document(file_path, doc_name):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".pdf":
            loader = PyPDFLoader(file_path)
        elif ext in [".md", ".txt"]:
            loader = TextLoader(file_path)
        else:
            raise ValueError("Unsupported file type")

        pages = loader.load_and_split()

        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(pages, embeddings)
        
        # Create unique index name based on document name
        safe_doc_name = "".join(c for c in doc_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_doc_name = safe_doc_name.replace(' ', '_')
        index_name = f"faiss_index_{safe_doc_name}"
        
        # Ensure the faiss_index directory exists in the project root
        index_dir = os.path.join(settings.BASE_DIR, "faiss_index")
        os.makedirs(index_dir, exist_ok=True)
        
        # Save the vectorstore with unique name
        index_path = os.path.join(index_dir, index_name)
        vectorstore.save_local(index_path)
        
        print(f"Successfully processed document: {doc_name}")
        print(f"FAISS index saved to: {index_path}")
        
    except Exception as e:
        print(f"Error processing document {doc_name}: {str(e)}")
        raise e
