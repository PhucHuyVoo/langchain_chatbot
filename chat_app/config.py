import os

from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#MongoDB
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATA_COLLECTION = os.getenv("MONGODB_DATA_COLLECTION")