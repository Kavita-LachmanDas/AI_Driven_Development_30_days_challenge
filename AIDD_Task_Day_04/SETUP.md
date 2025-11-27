# Setup Instructions

## Prerequisites
- Python 3.8 or higher
- Google Gemini API Key

## Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the API key

3. **Configure Environment Variables**
   - Create a `.env` file in the project root directory
   - Add your API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - Note: The `.env` file is already in `.gitignore` to keep your API key secure
   - You can use `.env.example` as a template

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Using the Application**
   - The API key will be automatically loaded from the `.env` file
   - Upload a PDF file
   - Click "Extract & Summarize" to generate a summary
   - Click "Generate Quiz" to create quiz questions

## Features

### PDF Summarizer
- Upload any PDF file
- Automatic text extraction using PyPDF
- AI-powered summary generation using Gemini
- Clean, formatted output

### Quiz Generator
- Generate multiple choice questions (MCQs)
- Mixed question types (True/False, Fill in the blank, Short answer)
- Questions based on the original PDF content
- Includes answer key

## Notes

- The application uses Google Gemini API for AI processing
- Context7 MCP integration can be added as an extension
- OpenAgents SDK integration can be implemented based on specific requirements

