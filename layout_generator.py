import requests
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from transformers import pipeline


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_layout_suggestion(text):
    classification_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["invoice", "resume", "article", "legal document", "research paper"]
    classification = classification_pipeline(text, candidate_labels=labels)
    doc_type = classification["labels"][0]  

    layout_suggestions = {
        "invoice": [
            "1. Company Logo & Details (Top Left)",
            "2. Invoice Number & Date (Top Right)",
            "3. Customer Details (Below Invoice Info)",
            "4. Table of Items & Prices",
            "5. Subtotal, Tax, and Grand Total",
            "6. Payment Terms & Notes"
        ],
        "resume": [
            "1. Name & Contact Details (Top Center)",
            "2. Summary/Profile Section",
            "3. Work Experience (Most Recent First)",
            "4. Skills & Certifications",
            "5. Education Background",
            "6. Projects & Achievements"
        ],
        "article": [
            "1. Title & Subtitle (Top Center)",
            "2. Author Name & Date (Below Title)",
            "3. Introduction Paragraph",
            "4. Body Content with Headings",
            "5. Conclusion & References",
            "6. Images & Figures"
        ],
        "legal document": [
            "1. Case Title & Reference Number (Top)",
            "2. Parties Involved",
            "3. Legal Clauses & Sections",
            "4. Terms & Conditions",
            "5. Signatures & Witnesses"
        ],
        "research paper": [
            "1. Title & Authors",
            "2. Abstract & Keywords",
            "3. Introduction & Background",
            "4. Methodology",
            "5. Results & Discussion",
            "6. Conclusion & References"
        ]
    }

    return doc_type, layout_suggestions.get(doc_type, ["No predefined layout available."])

def visualize_layout(layout_steps):
    fig, ax = plt.subplots(figsize=(5, len(layout_steps) * 0.5))
    ax.set_title("Suggested Document Layout", fontsize=14, fontweight='bold')
    
    for i, step in enumerate(layout_steps):
        ax.text(0.1, 1 - (i / len(layout_steps)), f"{i+1}. {step}", fontsize=12, verticalalignment='top')
    
    ax.axis("off")
    return fig
