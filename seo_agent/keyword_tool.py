import requests
from config import SERPAPI_KEY

def get_keywords(topic):
    url = f"https://serpapi.com/search.json?q={topic}&api_key={SERPAPI_KEY}"
    res = requests.get(url).json()
    keywords = [s['query'] for s in res.get('related_questions', []) if 'query' in s]
    return keywords or [topic]
