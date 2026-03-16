# 🤖 AI-Powered Candidate Ranking & Resume Analytics System

Welcome to my end-to-end Data Science project! This repository showcases the journey of building an automated hiring tool—from initial data exploration to a fully functional web application.

### 🚀 [Live Demo - Click Here to Try the App](https://ai-candidate-ranker-system-ljpy3iwpj4nrqq59fp4bnh.streamlit.app/)

---

## 📊 Project Visualization
Below is a snapshot of the AI Candidate Ranker dashboard in action:

![App Demo](app-visual.png)

---

## 🏗️ System Architecture
The following diagram explains the internal workflow of the system (Auto-rendered via Mermaid):

## 🏗️ System Architecture
The following diagram explains the internal workflow of the system:
---

## 👤 Developed By
**Zannatul Sanzida** *Aspiring Data Professional | Computer Science & Engineering*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zannatul-sanzida-705a71203/)  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ZannatUSM)
```mermaid
graph LR
    A[User/Recruiter] -->|Uploads Job Description| B(Streamlit App)
    A -->|Uploads Multiple PDF Resumes| B
    B --> C{NLP Engine}
    C --> D[Text Extraction - PyPDF2]
    D --> E[Text Cleaning & Tokenization]
    E --> F[TF-IDF Vectorization]
    F --> G[Cosine Similarity Calculation]
    G --> H[Ranking Results Dashboard]
    H --> I[Candidate Evaluation]


