import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("API key not found. Make sure it's set in the .env file.")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the new supported model
    messages=[
        {"role": "user", "content": "Hello, what can you do?"}
    ],
    max_tokens=50
)

print(response['choices'][0]['message']['content'])
