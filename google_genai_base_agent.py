from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="I have started my agentic AI Journey, this is my first base agent. Will you help me in my journey?"
)
print(response.text)