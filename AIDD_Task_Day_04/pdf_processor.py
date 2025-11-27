"""
PDF Processor Module
Handles PDF text extraction using PyPDF
"""

from pypdf import PdfReader
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFProcessor:
    """Class to handle PDF text extraction"""
    
    def __init__(self):
        self.reader = None
    
    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text as a string
        """
        try:
            logger.info(f"Extracting text from PDF: {pdf_path}")
            reader = PdfReader(pdf_path)
            
            text_content = []
            total_pages = len(reader.pages)
            
            for page_num in range(total_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text.strip():
                    text_content.append(text)
            
            full_text = "\n\n".join(text_content)
            logger.info(f"Successfully extracted text from {total_pages} pages")
            
            return full_text
            
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {str(e)}")
            raise Exception(f"Failed to extract text from PDF: {str(e)}")
    
    def get_page_count(self, pdf_path: str) -> int:
        """
        Get the number of pages in a PDF
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Number of pages
        """
        try:
            reader = PdfReader(pdf_path)
            return len(reader.pages)
        except Exception as e:
            logger.error(f"Error getting page count: {str(e)}")
            return 0

