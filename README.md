# streamlit-gemini-doc-processor

This project is a Streamlit application that utilizes the Gemini API to process uploaded documents. Users can input prompts such as "make a summary" to generate summaries of the submitted documents.

## Project Structure

```
streamlit-gemini-doc-processor
├── src
│   ├── app.py                # Main entry point for the Streamlit application
│   ├── utils
│   │   ├── __init__.py       # Initializes the utils package
│   │   ├── document_processor.py # Functions for processing uploaded documents
│   │   └── gemini_client.py   # Class for handling API calls to the Gemini API
│   └── config
│       ├── __init__.py       # Initializes the config package
│       └── settings.py       # Configuration settings such as API keys
├── requirements.txt          # Lists project dependencies
├── .env                      # Stores environment variables
├── .gitignore                # Specifies files to ignore by Git
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-gemini-doc-processor
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file. Make sure to include your API keys and any other sensitive information.

5. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage

- Upload a document using the provided interface.
- Enter your prompt (e.g., "make a summary") to interact with the Gemini API.
- View the generated summaries or responses directly in the Streamlit app.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
