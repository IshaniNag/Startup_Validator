# modules/scoring.py

import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def calculate_score(idea, sentiment_score, trend_scores):
    """
    Hybrid scoring:
    - 60% from Cohere (based on full startup idea)
    - 20% from sentiment (scaled from [-1,1] to [0,100])
    - 20% from average trend score (0-100)
    """

    # Call Cohere to get a score
    cohere_prompt = f"""
    You are a startup validation expert. Score the following startup idea from 0 to 100.
    Only return the number.

    Startup Idea:
    {idea}
    """

    try:
        response = co.generate(
            prompt=cohere_prompt,
            model="command-r-plus",
            max_tokens=5,
            temperature=0.5
        )
        cohere_score = int(''.join(filter(str.isdigit, response.generations[0].text.strip())))
        cohere_score = min(max(cohere_score, 0), 100)
    except Exception as e:
        print("Cohere scoring failed:", e)
        cohere_score = 50

    # Normalize sentiment score from [-1, 1] → [0, 100]
    sentiment_component = ((sentiment_score + 1) / 2) * 100

    # Average trend score
    if trend_scores:
        avg_trend = sum(trend_scores.values()) / len(trend_scores)
    else:
        avg_trend = 0

    # Final weighted score
    final_score = (
        0.6 * cohere_score +
        0.2 * sentiment_component +
        0.2 * avg_trend
    )

    return round(min(max(final_score, 0), 100), 2)
def explain_score(idea):
    prompt = f"""
    You're a startup evaluator. Give a 2-3 sentence explanation of why this startup idea might succeed or fail based on market trends, innovation, and competition.

    Idea:
    {idea}

    Explanation:
    """

    try:
        response = co.generate(
            prompt=prompt,
            model="command-r-plus",
            max_tokens=100,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return "Explanation not available due to an error."
