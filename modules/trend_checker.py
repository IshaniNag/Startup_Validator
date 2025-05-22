# from pytrends.request import TrendReq
# import time

# def get_trend_scores(keywords):
#     pytrends = TrendReq(hl='en-US', tz=360)
#     trend_scores = {}

#     for keyword in keywords:
#         keyword = keyword.lower().strip()
#         try:
#             pytrends.build_payload([f'"{keyword}"'], timeframe='today 12-m')
#             data = pytrends.interest_over_time()

#             if not data.empty and data[keyword].sum() > 0:
#                 trend_scores[keyword] = int(data[keyword].iloc[-1])
#             else:
#                 trend_scores[keyword] = 30  # fallback score for low/no data
#         except Exception as e:
#             print(f"Error fetching trend for '{keyword}': {e}")
#             trend_scores[keyword] = 0

#         time.sleep(3)

#     return trend_scores

import random

def get_trend_scores(keywords):
    trend_scores = {}

    for keyword in keywords:
        keyword = keyword.lower().strip()
        # Randomly assign a trend score between 30 and 100
        trend_scores[keyword] = random.randint(30, 100)

    return trend_scores

# Example usage:
# keywords = ['ai', 'mental health', 'college students', 'virtual therapy']
# print(get_trend_scores(keywords))
