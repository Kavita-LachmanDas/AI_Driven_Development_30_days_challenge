# Study Notes Summarizer & Quiz Generator Agent

A Streamlit-based chatbot application that uses AI to summarize PDF study materials and generate quiz questions.

## Features

### 📄 PDF Summarizer
- Upload PDF files of any size
- Automatic text extraction using PyPDF
- AI-powered summary generation using Google Gemini
- Clean, well-formatted summaries with headings and bullet points

### 🎯 Quiz Generator
- Generate multiple choice questions (MCQs)
- Mixed question types (True/False, Fill in the blank, Short answer)
- Questions based on the original PDF content (not the summary)
- Includes answer keys for all questions

## Technology Stack

- **Streamlit**: Modern web UI framework
- **PyPDF**: PDF text extraction
- **Google Gemini API**: AI-powered summarization and quiz generation
- **Python 3.8+**: Core programming language

## Installation

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get a Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the API key for use in the application

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Configure the application**
   - Enter your Gemini API Key in the sidebar
   - The API key is stored in session state (not saved permanently)

3. **Upload and process PDFs**
   - Click "Choose a PDF file" to upload your study material
   - Click "Extract & Summarize" to generate a summary
   - Click "Generate Quiz" to create quiz questions

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── pdf_processor.py       # PDF text extraction module
├── agent_handler.py       # AI agent handler (Gemini integration)
├── context7_mcp.py        # Context7 MCP integration placeholder
├── requirements.txt       # Python dependencies
├── SETUP.md              # Detailed setup instructions
└── PROJECT_README.md     # This file
```

## How It Works

1. **PDF Upload**: User uploads a PDF file through the Streamlit interface
2. **Text Extraction**: PyPDF extracts all text content from the PDF
3. **Summary Generation**: Gemini AI analyzes the text and creates a structured summary
4. **Quiz Generation**: Gemini AI generates quiz questions based on the original PDF content

## Requirements

- Python 3.8 or higher
- Google Gemini API Key (free tier available)
- Internet connection for API calls

## Notes

- **Context7 MCP Integration**: A placeholder module (`context7_mcp.py`) is included for future Context7 MCP tool provider integration
- **OpenAgents SDK**: Can be integrated based on specific requirements
- **API Limits**: Be aware of Gemini API rate limits and token limits
- **File Size**: Large PDFs may be truncated to fit within API token limits

## Troubleshooting

### "Failed to extract text from PDF"
- Ensure the PDF is not password-protected
- Check if the PDF contains actual text (not just images)
- Try a different PDF file

### "Failed to generate summary/quiz"
- Verify your API key is correct
- Check your internet connection
- Ensure you haven't exceeded API rate limits

### Application won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

## License

This project is created for educational purposes as part of the AI-Driven Development course.

## Future Enhancements

- [ ] Context7 MCP full integration
- [ ] OpenAgents SDK integration
- [ ] Support for multiple PDF formats
- [ ] Export summaries and quizzes to files
- [ ] Customizable quiz question count
- [ ] Support for image-based PDFs (OCR)

