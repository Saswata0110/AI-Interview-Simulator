from rag.embedding import ResumeEmbedding

text = """
Python Flask MySQL REST API Docker
TensorFlow Machine Learning
This is my first AI Interview Simulator project.
"""

embedding = ResumeEmbedding()

chunks = embedding.split_text(text)

vectors = embedding.create_embeddings(chunks)

print("Chunks:")
print(chunks)

print()

print("Embedding Shape:")
print(vectors.shape)