import streamlit as st
import asyncio
from utils import (
    extract_text, summarize_text, ask_question, extract_named_entities, 
    extract_tables, analyze_sentiment, extract_keywords, classify_document, translate_text
)
from layout_generator import generate_layout_suggestion, visualize_layout

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

st.set_page_config(page_title="AI Document Processor", page_icon="📄", layout="wide")

st.sidebar.title("📄 DocMiner: AI Document Processor")
st.sidebar.markdown("**An AI-powered tool to process, analyze, and extract insights from documents.**")

uploaded_file = st.sidebar.file_uploader("📂 Upload Document", type=["pdf", "txt", "jpg", "png", "mp3", "wav"])

st.markdown("<h1 style='text-align: center; color: #2D336B;'>📄 DocMiner: AI-Powered Document Processor</h1>", unsafe_allow_html=True)

tabs = st.tabs(["🔍 Extract & Analyze", "📊 AI Insights", "🌍 Translation", "📑 Layout Suggestion"])

if uploaded_file:
    with st.spinner("Processing document..."):
        extracted_text = extract_text(uploaded_file)

    with tabs[0]:
        st.subheader("📜 Extracted Text")
        st.expander("View Extracted Text").write(extracted_text)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏷️ Extract Named Entities"):
                with st.spinner("Extracting..."):
                    entities = extract_named_entities(extracted_text)
                st.subheader("📌 Named Entities")
                for word, entity_type in entities:
                    st.write(f"**{word}** → {entity_type}")

            if st.button("📊 Extract Tables"):
                with st.spinner("Extracting tables..."):
                    tables = extract_tables(uploaded_file)
                st.subheader("📑 Extracted Tables")
                if tables:
                    for table in tables:
                        st.table(table)
                else:
                    st.write("No tables found.")

        with col2:
            if st.button("😊 Analyze Sentiment"):
                with st.spinner("Analyzing sentiment..."):
                    sentiment = analyze_sentiment(extracted_text)
                st.subheader("📊 Sentiment Analysis")
                st.write(f"Sentiment: **{sentiment['label']}** (Confidence: {sentiment['score']:.2f})")

            if st.button("🔑 Extract Keywords"):
                with st.spinner("Extracting keywords..."):
                    keywords = extract_keywords(extracted_text)
                st.subheader("🔑 Key Terms")
                st.write(keywords)

    with tabs[1]:
        st.subheader("✂️ AI-Powered Summarization")
        if st.button("Summarize Document"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(extracted_text)
            st.write("📌 Summary")
            st.success(summary)

        st.subheader("🤖 Ask AI About the Document")
        user_question = st.text_input("Ask a question:")
        if user_question:
            with st.spinner("Thinking..."):
                answer = ask_question(user_question, extracted_text)
            st.write("🤖 Answer")
            st.info(answer)

        if st.button("📂 Classify Document"):
            with st.spinner("Classifying document..."):
                classification = classify_document(extracted_text)
            st.subheader("📌 Document Type")
            st.success(classificatio
                       
    with tabs[2]:
        st.subheader("🔄 Translate Document")
        target_lang = st.selectbox("Choose Language", ["French", "Spanish", "German", "Chinese", "Arabic"], index=0)
        if st.button("Translate Text"):
            with st.spinner("Translating..."):
                translated_text = translate_text(extracted_text, target_lang[:2].lower())  # Convert to language code
            st.subheader("📜 Translated Text")
            st.success(translated_text)

    with tabs[3]:
        if st.button("📑 Generate Layout Suggestion"):
            with st.spinner("Analyzing document structure..."):
                doc_type, layout_steps = generate_layout_suggestion(extracted_text)
            st.subheader(f"📑 Suggested Layout for **{doc_type.capitalize()}**")
            for step in layout_steps:
                st.write(f"- {step}")

            st.pyplot(visualize_layout(layout_steps))

else:
    st.info("📂 Please upload a document to start processing.")
