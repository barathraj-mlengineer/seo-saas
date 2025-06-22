import requests
from config import SERPAPI_KEY

def get_image_url(topic):
    params = {
        "engine": "google_images",
        "q": topic,
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get("https://serpapi.com/search.json", params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad status
        data = response.json()
        return data["images_results"][0]["original"]
    except (requests.RequestException, KeyError, IndexError):
        return "https://via.placeholder.com/600x400?text=Image+Not+Found"
