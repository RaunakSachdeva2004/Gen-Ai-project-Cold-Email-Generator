# 📧 Cold Email Generator

A Generative AI application designed to help software services companies and freelancers automate their cold outreach. By analyzing a potential client's job posting URL, this tool identifies their specific needs and generates a personalized cold email that showcases relevant projects from your portfolio.

## 📖 Overview

The Cold Email Generator streamlines the business development process. Instead of sending generic templates, this tool:

- Scrapes the job description from a provided URL.
- Analyzes the requirements using an LLM.
- Matches those requirements with the most relevant case studies from your vector database (`my_portfolio.csv`).
- Generates a tailored email that positions your services as the perfect solution.

## ✨ Key Features

- **⚡ Ultra-Fast Generation**: Powered by Groq's LPU inference engine for near-instant email generation.
- **🧠 Context-Aware**: Extracts specific skills and keywords from job descriptions to ensure relevance.
- **📂 Portfolio Integration**: Dynamically pulls the most relevant projects from your portfolio to back up your claims.
- **🕸️ Web Scraping**: Automatically fetches content from career pages using LangChain loaders.
- **🎨 Clean UI**: Built with Streamlit for an easy-to-use interactive interface.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM Engine**: Groq (using Llama 3)
- **Orchestration**: LangChain
- **Vector Database**: ChromaDB
- **Data Source**: CSV (Portfolio Data)

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.10 or higher
- A Groq Cloud API Key

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RaunakSachdeva2004/Gen-Ai-project-Cold-Email-Generator.git
   cd Gen-Ai-project-Cold-Email-Generator
   ```

## Set up Environment
  ```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

## 3. Install Dependencies
``` bash
pip install -r requirements.txt
```

## 4. Configure API Keys

Create a .env file in the root directory and add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

## 🏃‍♂️ Usage

- Prepare Your Portfolio

Update my_portfolio.csv with your own projects, tech stacks, and links. This is the data the AI uses to prove your expertise.

- Run the Application
```bash
  streamlit run app/main.py
  ```
## 3. Generate Emails

- Open the local Streamlit URL (usually http://localhost:8501).

- Paste the URL of a job posting (e.g., from a company's career page).

- Click Submit.

- The tool will display the scraped job description and the generated cold email.

## 📂 Project Structure
```bash
Gen-Ai-project-Cold-Email-Generator/
├── app/
│   ├── main.py          # Main Streamlit application
│   ├── chains.py        # LLM chains and prompt templates
│   ├── portfolio.py     # Logic for querying ChromaDB
│   └── utils.py         # Utility functions (text cleaning, scraping)
├── my_portfolio.csv     # Database of your projects/case studies
├── requirements.txt     # Python dependencies
├── .env                 # API keys (excluded from git)
└── README.md            # Project documentation
```

## 📄 License
This project is open-source.

