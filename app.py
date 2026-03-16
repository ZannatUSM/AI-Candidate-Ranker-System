import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import pandas as pd

# Function to safely extract text from PDF files
def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        # Returns an empty string if the file is corrupted or unreadable
        return ""

# Function to calculate similarity score using TF-IDF and Cosine Similarity
def get_match_score(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0
    
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        # Vectorize both texts into a shared matrix
        tfidf_matrix = vectorizer.fit_transform([str(resume_text), str(jd_text)])
        # Compute cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        return round(similarity[0][0] * 100, 2)
    except Exception as e:
        return 0

# Page Configuration
st.set_page_config(page_title="AI Candidate Ranker", layout="wide")

# UI Headers
st.title("🏆 AI Candidate Ranker & Resume Matcher")
st.markdown("### Screen multiple resumes efficiently with NLP-powered analysis.")

# Input Section
st.divider()
jd_input = st.text_area("💼 Paste Job Description", height=200, placeholder="Enter the job requirements here...")
uploaded_files = st.file_uploader("📄 Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

# Main Processing Logic
if st.button("Rank Candidates "):
    if uploaded_files and jd_input:
        results = []
        
        # Progress bar for better user experience
        progress_bar = st.progress(0)
        
        for index, file in enumerate(uploaded_files):
            # Extract text with error handling
            resume_text = extract_text_from_pdf(file)
            
            # Calculate score
            score = get_match_score(resume_text, jd_input)
            
            results.append({
                "Candidate Name": file.name, 
                "Match Score (%)": score
            })
            
            # Update progress bar
            progress_bar.progress((index + 1) / len(uploaded_files))
        
        # Create DataFrame and Sort by Score
        df_results = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        
        # Display Results
        st.divider()
        st.subheader(" Ranking Results")
        
        # Highlight the best candidate
        if not df_results.empty:
            st.table(df_results)
            
            best_candidate = df_results.iloc[0]["Candidate Name"]
            best_score = df_results.iloc[0]["Match Score (%)"]
            
            if best_score > 0:
                st.success(f"🥇 **Best Match:** {best_candidate} with a score of {best_score}%")
            else:
                st.warning("No significant matches found. Please check the inputs.")
        
    else:
        st.error("Please provide both a job description and at least one resume.")