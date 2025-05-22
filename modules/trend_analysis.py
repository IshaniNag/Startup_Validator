from pytrends.request import TrendReq

def analyze_trends(keywords):
    """
    Analyze the current trends of the provided keywords using Google Trends API.
    """
    pytrends = TrendReq(hl='en-US', tz=360)  # Initialize Google Trends API with time zone 360 (UTC+6)
    
    # Get the Google Trends interest over time for the keywords
    pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='', gprop='')
    
    try:
        # Get interest over time data from Google Trends
        interest_over_time_df = pytrends.interest_over_time()
        
        if interest_over_time_df.empty:
            return {keyword: 0 for keyword in keywords}  # Return a score of 0 if no trends found
        
        # Calculate trend score for each keyword
        trend_scores = {}
        for keyword in keywords:
            trend_scores[keyword] = interest_over_time_df[keyword].mean()  # Average trend score over the past week
        
        return trend_scores
    except Exception as e:
        return {"error": f"An error occurred while fetching trends: {str(e)}"}
