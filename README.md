# 📄 DocMiner: AI-Powered Document Processing Tool

## Overview
DocMiner is a Streamlit-based AI tool that extracts text, summarizes documents, and answers questions using the Groq API. It supports PDF, DOCX, and TXT files, making document analysis faster and more efficient. 🚀
## Features

* Upload Documents – Supports PDF, DOCX, and TXT files
* Extract Text – AI-powered OCR and text extraction
* Summarization – Summarizes large documents into concise points
* Question Answering – Ask questions based on document contents
* Layout Generation – Automatically generates structured layouts
* Easy-to-Use Interface – Built with Streamlit for simplicity


## Project Structure
```
DocMiner/
│── .env                    # Stores API keys (DO NOT SHARE)
│── app.py                  # Streamlit UI
│── utils.py                # Core AI processing logic
│── requirements.txt        # Dependencies
│── README.md               # This file
└── sample_docs/            # Optional

```


## Setup Instructions

### Prerequisites

Ensure you have:
* Python 3.8+ installed.
* A valid GROQ API Key ([Get from here](https://console.groq.com/keys)).
* Huggingface Access Token ([Get from here](https://huggingface.co/settings/tokens)).


### Clone Repository
```
git clone https://github.com/taufeeq-mustafa/DocMiner.git
cd DocMiner
```
### Create & Activate a Virtual Environment
```
python -m venv venv
venv\Scripts\activate  
```

### Install Dependancies
```
pip install -r requirements.txt
```


### Run the Project
```
python -m streamlit run app.py
```




    
## License

[MIT](https://choosealicense.com/licenses/mit/)

