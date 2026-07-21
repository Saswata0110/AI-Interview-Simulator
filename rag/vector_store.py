import os
import pickle

import faiss
import numpy as np

from rag.embedding import ResumeEmbedding


class ResumeVectorStore:

    def __init__(self):

        self.embedding = ResumeEmbedding()

        self.index = None

        self.chunks = []

    def create_vector_store(self, text):

        # Split resume into chunks
        self.chunks = self.embedding.split_text(text)

        # Generate embeddings
        vectors = self.embedding.create_embeddings(self.chunks)

        dimension = vectors.shape[1]

        # Create FAISS index
        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(vectors.astype(np.float32))

        os.makedirs("faiss_index", exist_ok=True)

        # Save FAISS index
        faiss.write_index(
            self.index,
            "faiss_index/index.faiss"
        )

        # Save text chunks
        with open("faiss_index/chunks.pkl", "wb") as f:
            pickle.dump(self.chunks, f)

    def load_vector_store(self):

        self.index = faiss.read_index(
            "faiss_index/index.faiss"
        )

        with open("faiss_index/chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)

    def search(self, query, top_k=3):

        query_vector = self.embedding.create_embeddings(
            [query]
        )

        distances, indices = self.index.search(
            query_vector.astype(np.float32),
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results