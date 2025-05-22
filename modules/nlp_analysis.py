# modules/nlp_analysis.py
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def extract_keywords(text, max_keywords=5):
    # Use generate to ask for keywords directly
    prompt = f"""
    Extract the top {max_keywords} most relevant keywords from the following startup idea:

    "{text}"
    
    Respond with a Python list of keywords (no index numbers, just words).
    """
    gen_response = co.generate(
        prompt=prompt,
        model="command-r-plus",
        max_tokens=100,
        temperature=0.5
    )
    try:
        keywords = eval(gen_response.generations[0].text.strip())
        return keywords
    except:
        return [text]  # fallback in case of error
