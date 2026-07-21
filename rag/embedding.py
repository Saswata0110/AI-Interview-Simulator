from sentence_transformers import SentenceTransformer


class ResumeEmbedding:
    """
    Handles text chunking and embedding generation.
    """

    def __init__(self):
        # Lightweight and accurate embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def split_text(self, text, chunk_size=500):
        """
        Split long resume text into chunks.
        """

        words = text.split()

        chunks = []

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)

        return chunks

    def create_embeddings(self, chunks):
        """
        Convert text chunks into embeddings.
        """

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings