from rag.vector_store import ResumeVectorStore

resume = """
Python
Flask
MySQL
REST API
TensorFlow

Projects

AI Interview Simulator using Flask, MySQL, FAISS and Gemini AI.

Skills

Python
Machine Learning
SQL
"""

vector_db = ResumeVectorStore()

vector_db.create_vector_store(resume)

print("Vector Database Created!")

vector_db.load_vector_store()

results = vector_db.search(
    "Tell me about Flask"
)

print()

print("Search Results:")

for r in results:
    print("---------------------------")
    print(r)