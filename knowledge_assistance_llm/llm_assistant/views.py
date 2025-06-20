from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from knowledge_base.models import Document
from django.conf import settings
import os
import glob


class AskQuestionView(APIView):
    def post(self, request):
        question = request.data.get("question")
        
        if not question:
            return Response({'error': 'No question provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check if any documents exist in database
            document_count = Document.objects.all().count()  # type: ignore[attr-defined]
            if document_count == 0:
                return Response({
                    'error': 'No documents found in database. Please upload some documents first through the admin panel.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Check if FAISS index directory exists
            index_dir = os.path.join(settings.BASE_DIR, "faiss_index")
            if not os.path.exists(index_dir):
                return Response({
                    'error': f'Knowledge base index not found. {document_count} document(s) exist in database but index was not created. Please try re-uploading a document.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Find all FAISS index files
            index_files = glob.glob(os.path.join(index_dir, "faiss_index_*"))
            if not index_files:
                return Response({
                    'error': f'FAISS index files not found. {document_count} document(s) exist but no index files were created. Please try re-uploading a document.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Use the first available index file
            index_path = index_files[0]
            print(f"Loading FAISS index from: {index_path}")

            # Load the vectorstore with security parameter
            vectorstore = FAISS.load_local(index_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

            # Create retriever and LLM chain
            retriever = vectorstore.as_retriever()
            qa_chain = RetrievalQA.from_chain_type(
                llm=OpenAI(),
                retriever=retriever,
                return_source_documents=True
            )

            result = qa_chain(question)
            sources = [doc.metadata.get('source', '') for doc in result['source_documents']]

            return Response({
                "answer": result['result'],
                "sources": sources
            })
            
        except Exception as e:
            return Response({
                'error': f'Error processing question: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
