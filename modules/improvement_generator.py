# modules/improvement_generator.py

import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_improvements(text):
    prompt = f"""
    Suggest 5 specific and practical ways to improve the following startup idea:

    "{text}"

    Format the response as a numbered list.
    """
    response = co.generate(
        prompt=prompt,
        model="command-r-plus",
        max_tokens=200,
        temperature=0.6
    )

    return response.generations[0].text.strip()
