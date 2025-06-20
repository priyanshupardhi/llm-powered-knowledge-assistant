# Knowledge Assistance LLM

A Django-based knowledge management system that allows you to upload documents and ask questions using AI-powered retrieval and language models.

## Features

- **Document Upload**: Upload PDF, TXT, and MD files through Django admin
- **Automatic Processing**: Documents are automatically processed and indexed using FAISS vector store
- **AI-Powered Q&A**: Ask questions about uploaded documents using OpenAI's language models
- **REST API**: Full API endpoints for document management and question answering
- **Vector Search**: Efficient semantic search using OpenAI embeddings

## Tech Stack

- **Backend**: Django 5.2.3
- **API**: Django REST Framework
- **AI/ML**: LangChain, OpenAI API
- **Vector Store**: FAISS
- **Database**: SQLite (default)
- **Document Processing**: PyPDF2, Text processing

## Prerequisites

- Python 3.8+
- OpenAI API key
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd KnowledgeAssistanceLLM
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Database Settings
DATABASE_URL=sqlite:///db.sqlite3

# Media and Static Files
MEDIA_URL=/media/
STATIC_URL=/static/
```

### 5. Database Setup

```bash
cd knowledge_assistance_llm
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

## Usage

### 1. Upload Documents

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Navigate to "Documents" section
4. Click "Add Document"
5. Upload your PDF, TXT, or MD file
6. The document will be automatically processed and indexed

### 2. Ask Questions

#### Via API

**Ask a question:**
```bash
curl -X POST http://127.0.0.1:8000/api/v1/llm-assistant/ask-question/ \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic of the document?"}'
```

**List uploaded documents:**
```bash
curl http://127.0.0.1:8000/api/v1/knowledge-base/documents/
```

#### API Endpoints

- `POST /api/v1/llm-assistant/ask-question/` - Ask questions about documents
- `GET /api/v1/knowledge-base/documents/` - List all uploaded documents

## Project Structure

```
knowledge_assistance_llm/
├── knowledge_assistance_llm/     # Main Django project
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   └── ...
├── knowledge_base/              # Document management app
│   ├── models.py               # Document model
│   ├── views.py                # API views
│   ├── utils.py                # Document processing
│   └── ...
├── llm_assistant/              # AI Q&A app
│   ├── views.py                # Question answering
│   └── ...
├── media/                      # Uploaded files
├── faiss_index/               # Vector store indexes
├── manage.py                   # Django management
└── requirements.txt           # Python dependencies
```

## Configuration

### OpenAI API Key

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Add it to your `.env` file as `OPENAI_API_KEY`

### Supported File Types

- **PDF**: Text extraction and processing
- **TXT**: Plain text files
- **MD**: Markdown files

## Troubleshooting

### Common Issues

1. **"FAISS index file not found"**
   - Make sure you've uploaded at least one document
   - Check that the document processing completed successfully
   - Re-upload the document if needed

2. **"OpenAI API key not found"**
   - Verify your `.env` file contains the correct API key
   - Ensure the key is valid and has sufficient credits

3. **"Module not found" errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check that your virtual environment is activated

### Debug Mode

Enable debug mode in `.env`:
```env
DEBUG=True
```

This will show detailed error messages and help with troubleshooting.

## Development

### Adding New File Types

To support additional file types, modify `knowledge_base/utils.py`:

```python
def process_document(file_path, doc_name):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext in [".md", ".txt"]:
        loader = TextLoader(file_path)
    elif ext == ".your_extension":
        loader = YourCustomLoader(file_path)
    else:
        raise ValueError("Unsupported file type")
```

### Customizing the AI Model

Modify the LLM configuration in `llm_assistant/views.py`:

```python
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0.7),  # Adjust temperature
    retriever=retriever,
    return_source_documents=True
)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the Django and LangChain documentation
3. Open an issue on GitHub

## Acknowledgments

- Django for the web framework
- LangChain for AI/ML integration
- OpenAI for language models
- FAISS for vector search capabilities 