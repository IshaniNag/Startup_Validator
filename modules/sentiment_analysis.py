# modules/sentiment_analysis.py

import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def analyze_sentiment(text):
    prompt = f"""
    Analyze the sentiment of the following startup idea and return a score between -1 (very negative) to +1 (very positive):

    "{text}"

    Just return the numeric sentiment score.
    """
    response = co.generate(
        prompt=prompt,
        model="command-r-plus",
        max_tokens=10,
        temperature=0.3,
    )

    try:
        score_text = response.generations[0].text.strip()
        score = float(score_text)
        return max(-1.0, min(score, 1.0))  # Clamp between -1 and 1
    except:
        return 0.0  # Neutral fallback
