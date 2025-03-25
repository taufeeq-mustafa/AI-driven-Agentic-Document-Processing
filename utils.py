import os
import pdfplumber
import pytesseract
import requests
import speech_recognition as sr
from PIL import Image
from dotenv import load_dotenv
from transformers import pipeline
from googletrans import Translator
from pydub import AudioSegment



load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


def extract_text(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file.type in ["image/png", "image/jpeg"]:
        image = Image.open(file)
        return pytesseract.image_to_string(image)
    else:
        return file.getvalue().decode("utf-8")
 

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def summarize_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  
        "messages": [{"role": "system", "content": "Summarize the following text:"},
                     {"role": "user", "content": text}],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)
    print("🔍 API Response:", response.json())

    if "choices" in response.json():
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "⚠️ Error: Unexpected API response. Check API key or request format."


def ask_question(question, text):
    url = "https://api.groq.com/openai/v1/chat/completions"  

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",  
        "messages": [
            {"role": "system", "content": "Answer based on the provided text."},
            {"role": "user", "content": f"Context: {text}\n\nQuestion: {question}"}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()  


    print("🔍 API Response:", response_data)
    if "choices" in response_data:
        return response_data["choices"][0]["message"]["content"]
    elif "error" in response_data:
        return f"⚠️ API Error: {response_data['error'].get('message', 'Unknown error')}"
    else:
        return "⚠️ Unexpected API response format."


def extract_named_entities(text):
    ner_pipeline = pipeline("ner", model="facebook/bart-large-cnn")
    entities = ner_pipeline(text)
    return [(entity["word"], entity["entity"]) for entity in entities]

def extract_tables(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            tables = [page.extract_table() for page in pdf.pages if page.extract_table()]
            return tables
    return []

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(text)[0]


def extract_keywords(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text, max_length=20, min_length=5, do_sample=False)[0]["summary_text"]

# Document Classification
def classify_document(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["invoice", "legal document", "article", "resume", "email"]
    return classifier(text, candidate_labels=labels)["labels"][0]

# Text Translation
def translate_text(text, target_lang="fr"):
    translator = Translator()
    return translator.translate(text, dest=target_lang).text


