from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("Gemini_Api_Key")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)