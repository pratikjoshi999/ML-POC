from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

print(openai_api_key)

openai = OpenAI()

messages = [{"role": "user", "content": "I have started my agentic AI Journey, this is my first base agent. Will you help me in my journey?"}]

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

print(response.choices[0].message.content)