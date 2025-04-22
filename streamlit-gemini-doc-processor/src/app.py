import streamlit as st
import PyPDF2
import docx
import google.generativeai as genai
import os
from dotenv import load_dotenv

class GeminiClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("API key not found. Please set GOOGLE_API_KEY in .env file")
        
        # Configure Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize model without additional configuration
        self.model = genai.GenerativeModel('gemini-pro')
    
    def send_request(self, document_text, prompt):
        try:
            combined_prompt = f"{prompt}\n\nDocument content:\n{document_text}"
            response = self.model.generate_content(combined_prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

def process_document(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    if file_type == 'txt':
        return uploaded_file.getvalue().decode('utf-8')
    
    elif file_type == 'pdf':
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    
    elif file_type == 'docx':
        doc = docx.Document(uploaded_file)
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
        return text
    
    return "Unsupported file format"

def main():
    st.title("Gemini Document Processor")
    
    uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])
    
    if uploaded_file is not None:
        document_text = process_document(uploaded_file)
        st.text_area("Document Text", document_text, height=300)
        
        prompt = st.text_input("Enter your prompt (e.g., 'make a summary'):")
        
        if st.button("Submit"):
            if prompt:
                client = GeminiClient()
                response = client.send_request(document_text, prompt)
                st.write("Response from Gemini API:")
                st.write(response)
            else:
                st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()