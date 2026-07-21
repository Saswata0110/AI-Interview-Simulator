from google import genai

from config import Config
from rag.vector_store import ResumeVectorStore
from rag.prompt import SYSTEM_PROMPT


class InterviewQA:

    def __init__(self):

        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

        self.vector_store = ResumeVectorStore()
        self.vector_store.load_vector_store()

    # ==========================
    # RAG (Resume Questions)
    # ==========================
    def ask(self, question):

        context = self.vector_store.search(
            question,
            top_k=3
        )

        if len(context) == 0:
            return "I couldn't find that information in the uploaded resume."

        context = "\n\n".join(context)

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question
        )

        try:

            response = self.client.models.generate_content(
                model="models/gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"Gemini Error: {e}"

    # ==========================
    # Direct Gemini (No RAG)
    # ==========================
    def chat(self, prompt):

        try:

            response = self.client.models.generate_content(
                model="models/gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error = str(e)

            if "RESOURCE_EXHAUSTED" in error or "429" in error:
                return (
                    "⚠️ Gemini API quota exceeded.\n\n"
                    "Please wait for the quota to reset or use another Gemini API key."
                )

            return f"Gemini Error: {error}"