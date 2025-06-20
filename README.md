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

## Sample Testing Files

To test the system, you can use these sample files. **Note: The system currently supports uploading one file at a time.**

### Sample Text File (`sample_document.txt`)
Create a file named `sample_document.txt` with the following content:

```
Artificial Intelligence and Machine Learning

Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines that work and react like humans. Some of the activities computers with artificial intelligence are designed for include speech recognition, learning, planning, and problem solving.

Machine Learning is a subset of AI that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

Key Concepts:
1. Neural Networks: Computing systems inspired by biological neural networks
2. Deep Learning: A subset of machine learning using neural networks with multiple layers
3. Natural Language Processing: Enabling computers to understand and interpret human language
4. Computer Vision: Teaching computers to interpret and understand visual information

Applications of AI and ML include:
- Virtual assistants (Siri, Alexa)
- Recommendation systems (Netflix, Amazon)
- Autonomous vehicles
- Medical diagnosis
- Fraud detection
- Language translation
```

### Sample Markdown File (`research_paper.md`)
Create a file named `research_paper.md` with the following content:

```markdown
# The Future of Artificial Intelligence

## Introduction
Artificial Intelligence has evolved significantly over the past decade, transforming various industries and reshaping how we interact with technology.

## Current State of AI
Modern AI systems can perform tasks that were once thought to be exclusively human, including:
- Natural language understanding
- Image and video recognition
- Complex decision making
- Creative content generation

## Machine Learning Applications
Machine learning algorithms are being used in:
1. **Healthcare**: Disease diagnosis and drug discovery
2. **Finance**: Risk assessment and fraud detection
3. **Education**: Personalized learning and automated grading
4. **Transportation**: Self-driving cars and traffic optimization

## Challenges and Considerations
Despite rapid advancement, AI faces several challenges:
- Ethical concerns about bias and fairness
- Privacy and data security issues
- Job displacement and economic impact
- Need for robust safety measures

## Future Prospects
The future of AI holds promise for:
- Enhanced human-AI collaboration
- Solving complex global challenges
- Improving quality of life
- Advancing scientific research
```

## Usage

### 1. Upload Documents

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Navigate to "Documents" section
4. Click "Add Document"
5. **Upload one file at a time** (PDF, TXT, or MD file)
6. The document will be automatically processed and indexed

**Important Notes:**
- **Single File Upload**: Currently, the system processes one file at a time
- **File Replacement**: Uploading a new document will create a new index; previous documents remain in the database
- **Supported Formats**: PDF, TXT, MD files only

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

### 3. Testing with Sample Questions

After uploading a sample document, try these questions:

**For AI/ML content:**
- "What is artificial intelligence?"
- "What are the applications of machine learning?"
- "What challenges does AI face?"
- "How does machine learning work?"

**For research paper content:**
- "What is the future of AI?"
- "What are the current applications of AI?"
- "What challenges does AI face?"
- "What are the prospects for AI development?"

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

4. **"Single file upload limitation"**
   - The system currently supports one file at a time
   - Each upload creates a new index
   - Previous documents remain in the database

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