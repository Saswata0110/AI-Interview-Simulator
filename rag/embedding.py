from sentence_transformers import SentenceTransformer


class ResumeEmbedding:

    def __init__(self):
        self.model = None

    def get_model(self):
        if self.model is None:
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
        return self.model

    def split_text(self, text, chunk_size=500):

        words = text.split()

        chunks = []

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)

        return chunks

    def create_embeddings(self, chunks):

        model = self.get_model()

        embeddings = model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings