"""
Agent Handler Module
Handles integration with OpenAgents SDK, Gemini CLI, and Context7 MCP
"""

import google.generativeai as genai
import os
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AgentHandler:
    """Class to handle agent operations using Gemini API"""
    
    def __init__(self, api_key: str):
        """
        Initialize the agent handler
        
        Args:
            api_key: Google Gemini API key
        """
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        logger.info("Agent handler initialized with gemini-2.5-flash")
    
    def generate_summary(self, text: str, max_length: int = 500) -> str:
        """
        Generate a clean, meaningful summary of the provided text
        
        Args:
            text: Text content to summarize
            max_length: Maximum length of the summary
            
        Returns:
            Generated summary as a string
        """
        try:
            logger.info("Generating summary...")
            
            # Truncate text if too long (Gemini has token limits)
            if len(text) > 30000:
                text = text[:30000] + "... [Content truncated]"
            
            prompt = f"""You are an expert study notes summarizer. Please create a clean, well-structured summary of the following content.

Requirements:
- Create a concise but comprehensive summary
- Use clear headings and bullet points where appropriate
- Highlight key concepts and important information
- Make it easy to read and understand
- Keep the summary focused and meaningful

Content to summarize:
{text}

Please provide a well-formatted summary:"""

            response = self.model.generate_content(prompt)
            summary = response.text
            
            logger.info("Summary generated successfully")
            return summary
            
        except Exception as e:
            logger.error(f"Error generating summary: {str(e)}")
            raise Exception(f"Failed to generate summary: {str(e)}")
    
    def generate_quiz(self, text: str, num_questions: int = 5) -> str:
        """
        Generate quiz questions (MCQs and mixed-style) from the provided text
        
        Args:
            text: Text content to generate quiz from
            num_questions: Number of questions to generate
            
        Returns:
            Generated quiz as a formatted string
        """
        try:
            logger.info("Generating quiz...")
            
            # Truncate text if too long
            if len(text) > 30000:
                text = text[:30000] + "... [Content truncated]"
            
            prompt = f"""You are an expert quiz generator. Please create a comprehensive quiz based on the following study material.

Requirements:
- Generate {num_questions} questions
- Mix different question types: Multiple Choice Questions (MCQs) and other formats (True/False, Fill in the blank, Short answer)
- Each MCQ should have 4 options with only one correct answer
- Questions should test understanding of key concepts
- Include the correct answers at the end
- Format the quiz clearly with proper numbering

Study material:
{text}

Please generate a well-formatted quiz:"""

            response = self.model.generate_content(prompt)
            quiz = response.text
            
            logger.info("Quiz generated successfully")
            return quiz
            
        except Exception as e:
            logger.error(f"Error generating quiz: {str(e)}")
            raise Exception(f"Failed to generate quiz: {str(e)}")

