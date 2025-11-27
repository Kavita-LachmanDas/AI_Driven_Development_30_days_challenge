import streamlit as st
import os
from dotenv import load_dotenv
from pdf_processor import PDFProcessor
from agent_handler import AgentHandler
import tempfile

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Page configuration
st.set_page_config(
    page_title="Study Notes Summarizer & Quiz Generator",
    page_icon="📚",
    layout="wide"
)

# Initialize session state
if 'pdf_text' not in st.session_state:
    st.session_state.pdf_text = None
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'quiz' not in st.session_state:
    st.session_state.quiz = None
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# Title and description
st.title("📚 Study Notes Summarizer & Quiz Generator Agent")
st.markdown("---")
st.markdown("### Upload a PDF to get started with summarization and quiz generation!")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Display API Key status
    if GEMINI_API_KEY:
        st.success("✅ API Key loaded from .env file")
    else:
        st.error("❌ API Key not found in .env file")
        st.info("Please create a .env file with: GEMINI_API_KEY=your_api_key_here")
    
    st.markdown("---")
    st.markdown("### Instructions")
    st.markdown("""
    1. Upload a PDF file
    2. Click 'Extract & Summarize' to get a summary
    3. Click 'Generate Quiz' to create questions
    """)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📄 PDF Upload")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload your study material PDF"
    )
    
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
        st.success(f"File uploaded: {uploaded_file.name}")
        
        # Extract text button
        if st.button("🔍 Extract & Summarize", type="primary", use_container_width=True):
            if not GEMINI_API_KEY:
                st.error("Please set GEMINI_API_KEY in your .env file!")
            else:
                with st.spinner("Extracting text and generating summary..."):
                    try:
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_path = tmp_file.name
                        
                        # Extract text from PDF
                        pdf_processor = PDFProcessor()
                        extracted_text = pdf_processor.extract_text(tmp_path)
                        
                        if extracted_text:
                            st.session_state.pdf_text = extracted_text
                            
                            # Generate summary using agent
                            agent_handler = AgentHandler(GEMINI_API_KEY)
                            summary = agent_handler.generate_summary(extracted_text)
                            st.session_state.summary = summary
                            
                            st.success("Summary generated successfully!")
                        else:
                            st.error("Failed to extract text from PDF. Please check if the PDF is valid.")
                        
                        # Clean up temp file
                        os.unlink(tmp_path)
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

with col2:
    st.header("📝 Summary")
    
    if st.session_state.summary:
        st.markdown("### Generated Summary:")
        st.markdown(st.session_state.summary)
        
        # Quiz generation button
        st.markdown("---")
        if st.button("🎯 Generate Quiz", type="primary", use_container_width=True):
            if not GEMINI_API_KEY:
                st.error("Please set GEMINI_API_KEY in your .env file!")
            elif st.session_state.pdf_text:
                with st.spinner("Generating quiz questions..."):
                    try:
                        agent_handler = AgentHandler(GEMINI_API_KEY)
                        quiz = agent_handler.generate_quiz(st.session_state.pdf_text)
                        st.session_state.quiz = quiz
                        st.success("Quiz generated successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error generating quiz: {str(e)}")
            else:
                st.error("Please extract and summarize the PDF first!")
    else:
        st.info("Upload a PDF and click 'Extract & Summarize' to see the summary here.")

# Quiz display section
if st.session_state.quiz:
    st.markdown("---")
    st.header("🎯 Generated Quiz")
    st.markdown(st.session_state.quiz)

