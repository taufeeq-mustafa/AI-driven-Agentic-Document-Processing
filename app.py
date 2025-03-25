import streamlit as st

import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from utils import (
    extract_text, summarize_text, ask_question, extract_named_entities, 
    extract_tables, analyze_sentiment, extract_keywords, classify_document, translate_text
)
from layout_generator import generate_layout_suggestion, visualize_layout

st.set_page_config(page_title="AI Document Processor", page_icon="📄")
st.title("📄 AI-Powered Document Processor")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "jpg", "png", "mp3", "wav"])

if uploaded_file:
    extracted_text = extract_text(uploaded_file)
    st.text_area("Extracted Text", extracted_text, height=250)

    
    if st.button("Summarize Document"):
        summary = summarize_text(extracted_text)
        st.write("### 📌 Summary")
        st.write(summary)


    user_question = st.text_input("Ask a question about the document:")
    if user_question:
        answer = ask_question(user_question, extracted_text)
        st.write("### 🤖 Answer")
        st.write(answer)

    if st.button("Extract Named Entities"):
        entities = extract_named_entities(extracted_text)
        st.write("### 🏷️ Named Entities")
        for word, entity_type in entities:
            st.write(f"**{word}** → {entity_type}")


    if st.button("Extract Tables"):
        tables = extract_tables(uploaded_file)
        st.write("### 📊 Extracted Tables")
        if tables:
            for table in tables:
                st.table(table)
        else:
            st.write("No tables found.")


    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment(extracted_text)
        st.write(f"### 😊 Sentiment: {sentiment['label']} (Confidence: {sentiment['score']:.2f})")

   
    if st.button("Extract Keywords"):
        keywords = extract_keywords(extracted_text)
        st.write("### 🔑 Key Terms")
        st.write(keywords)

 
    if st.button("Classify Document"):
        classification = classify_document(extracted_text)
        st.write("### 📂 Document Type")
        st.write(classification)

    target_lang = st.selectbox("Translate to:", ["fr", "es", "de", "zh", "ar"])
    if st.button("Translate Text"):
        translated_text = translate_text(extracted_text, target_lang)
        st.write("### 🌍 Translated Text")
        st.write(translated_text)

    if st.button("Generate Layout Suggestion"):
        doc_type, layout_steps = generate_layout_suggestion(extracted_text)
        st.write(f"### 📑 Suggested Layout for **{doc_type.capitalize()}**")
        for step in layout_steps:
            st.write(f"- {step}")

       
        fig = visualize_layout(layout_steps)
        st.pyplot(fig)

