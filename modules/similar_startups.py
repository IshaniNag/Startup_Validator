import cohere
import os
import json
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def find_similar_startups(keyword_or_idea):
    prompt = f"""
    You are an expert startup advisor.

    A user has an idea related to: "{keyword_or_idea}".

    Your task is to suggest 3 existing startups that are most similar **in domain, product offering, and functionality**.

    Avoid listing general social media platforms like Snapchat, Instagram, TikTok unless the idea is explicitly social in nature.

    Make sure to not list dating platforms like Hinge, Bumble, Tinder etc. unless the idea is related to such platforms.

    Respond in JSON format like this:
    [
      {{"name": "Startup Name", "url": "https://startupwebsite.com"}},
      ...
    ]
    """

    try:
        response = co.generate(
            prompt=prompt,
            model="command-r-plus",
            max_tokens=300,
            temperature=0.6
        )

        output = response.generations[0].text.strip()

        # Clean up and safely parse JSON
        if output.startswith("```json"):
            output = output.split("```json")[1].split("```")[0].strip()
        elif output.startswith("```"):
            output = output.split("```")[1].split("```")[0].strip()

        similar = json.loads(output)

        # Filter out irrelevant results
        blacklist = ["TikTok", "Snapchat", "Instagram"]
        filtered = [s for s in similar if s["name"] not in blacklist]

        return filtered

    except Exception as e:
        print(f"Error parsing similar startups: {e}")
        return []
