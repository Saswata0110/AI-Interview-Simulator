import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = "supersecretkey123"

    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")