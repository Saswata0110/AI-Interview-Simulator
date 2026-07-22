# 🤖 AI Interview Simulator

An AI-powered Interview Simulator built using **Flask**, **MySQL**, **Google Gemini API**, **FAISS**, and **Sentence Transformers**. This application helps users prepare for technical interviews by generating resume-based interview questions, analyzing resumes, matching resumes with job descriptions, and providing AI-powered interview feedback using Retrieval-Augmented Generation (RAG).

---

# ✨ Features

## 🔐 Authentication
- User Registration
- Secure Login
- Logout
- Session Management

## 📄 Resume Upload
- Upload Resume in PDF Format
- Extract Resume Text
- Store Resume Information

## 🤖 AI Assistant
- Resume-aware AI Chatbot
- Context-based Question Answering
- Powered by Google Gemini API

## 🧠 Resume-based RAG
- Resume Chunking
- Sentence Transformer Embeddings
- FAISS Vector Search
- Semantic Resume Retrieval

## 🎤 AI Interview Simulator
- Resume-based Interview Questions
- Technical Questions
- Project Questions
- Behavioral Questions
- AI Evaluation
- Final Interview Report

## 📊 Resume Analysis
- Resume Strengths
- Resume Weaknesses
- Skill Gap Analysis
- Improvement Suggestions

## 📑 Job Description Matching
- ATS-style Resume Matching
- Match Percentage
- Missing Skills
- Resume Improvement Suggestions
- Interview Questions Based on JD

## 👤 User Dashboard
- Profile Management
- Resume History
- Interview History

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## Database
- MySQL

## Artificial Intelligence
- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Sentence Transformers
- all-MiniLM-L6-v2

## Python Libraries
- Flask
- Flask-MySQLdb
- PyMuPDF
- FAISS
- Sentence Transformers
- NumPy
- Google GenAI SDK
- ReportLab

---

# 📂 Project Structure

```
AI-Interview-Simulator
│
├── database/
├── forms/
├── models/
├── rag/
│   ├── embedding.py
│   ├── prompt.py
│   ├── qa.py
│   └── vector_store.py
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── resume.py
│   ├── interview.py
│   ├── chat.py
│   ├── jd_match.py
│   ├── resume_analysis.py
│   └── profile.py
│
├── services/
├── static/
├── templates/
├── utils/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Working Flow

1. User creates an account.
2. User logs into the system.
3. Resume is uploaded in PDF format.
4. Resume text is extracted.
5. Resume is divided into smaller chunks.
6. Sentence Transformers generate embeddings.
7. Embeddings are stored in a FAISS Vector Database.
8. User interacts with the AI Assistant.
9. Relevant resume information is retrieved using RAG.
10. Google Gemini generates intelligent responses.
11. AI Interview Simulator generates interview questions.
12. Candidate answers are evaluated.
13. AI generates a professional interview report.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Saswata0110/AI-Interview-Simulator.git
```

## Move into Project Folder

```bash
cd AI-Interview-Simulator
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Project

Update the following values inside `config.py`.

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

MYSQL_HOST = "localhost"

MYSQL_USER = "root"

MYSQL_PASSWORD = "your_password"

MYSQL_DB = "database_name"

SECRET_KEY = "your_secret_key"
```

## Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## 🏠 Home Page

_Add Screenshot_

---

## 🔑 Login Page

_Add Screenshot_

---

## 📊 Dashboard

_Add Screenshot_

---

## 📄 Resume Upload

_Add Screenshot_

---

## 🤖 AI Assistant

_Add Screenshot_

---

## 🎤 AI Interview

_Add Screenshot_

---

## 📑 Resume Analysis

_Add Screenshot_

---

## 📈 JD Match

_Add Screenshot_

---

## 📝 Final Interview Report

_Add Screenshot_

---

# 🔮 Future Improvements

- Voice-based AI Interview
- Coding Interview Module
- Multi-language Support
- Resume Builder
- AI Career Guidance
- Cloud Deployment
- Real-time Interview Analytics
- Interview Progress Tracking
- AI Mock Interview with Voice

---

# 📚 Learning Outcomes

This project helped me gain practical experience in:

- Flask Web Development
- REST API Development
- User Authentication
- Session Management
- MySQL Database Integration
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Sentence Transformers
- Google Gemini API
- Prompt Engineering
- Artificial Intelligence Integration
- Full Stack Development

---

# 💻 Author

**Saswata Dhar**

B.Tech in Computer Science & Engineering

GitHub:
https://github.com/Saswata0110

LinkedIn:
https://www.linkedin.com/

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Show Your Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
