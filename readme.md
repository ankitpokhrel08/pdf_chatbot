# RAG Gemini Chatbot

This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) chatbot using LangChain and Google Generative AI. The chatbot is designed to answer questions based on the content of a PDF document.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/RAG_Gemini.git
   cd RAG_Gemini
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your Google API key:
   ```env
   GEMINI_API_KEY=your_google_api_key
   ```

## Usage

1. **Run the Jupyter Notebook:**
   ```sh
   jupyter notebook
   ```

2. **Open `githubchatbot.ipynb` or `newchatbot copy.ipynb` and execute the cells sequentially.**

## Project Structure

```
RAG_Gemini/
├── pdfs/
│   └── Ankit_Resume.pdf
├── githubchatbot.ipynb
├── newchatbot copy.ipynb
├── readme.md
├── requirements.txt
└── .env
```

- **pdfs/**: Directory containing the PDF documents.
- **githubchatbot.ipynb**: Jupyter Notebook for the initial chatbot implementation.
- **newchatbot copy.ipynb**: Jupyter Notebook for the updated chatbot implementation.
- **readme.md**: This README file.
- **requirements.txt**: List of required Python packages.
- **.env**: Environment variables file (not included in the repository).

## How It Works

1. **Load and Split PDF:**
   - The PDF document is loaded using `PyPDFLoader`.
   - The document is split into smaller chunks using `RecursiveCharacterTextSplitter`.

2. **Generate Embeddings:**
   - Embeddings for each chunk are generated using `GoogleGenerativeAIEmbeddings`.

3. **Store Embeddings Locally:**
   - The embeddings and corresponding text chunks are stored in a JSON file (`data.json`).

4. **Retrieve Relevant Documents:**
   - When a user query is received, it is converted into embeddings.
   - The stored embeddings are compared with the query embeddings to find the most relevant documents.

5. **Generate Response:**
   - A prompt is created using the relevant documents and the user query.
   - The prompt is sent to the Google Generative AI model to generate a response.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
