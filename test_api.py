from google import genai
from config import Config

client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Say hello"
)

print(response.text)