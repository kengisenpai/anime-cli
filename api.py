import requests

BASE_URL = "https://api.jikan.moe/v4"

def search_anime(query):
    response = requests.get(f"{BASE_URL}/anime", params={"q": query})
    return response.json().get("data", [])

def get_top_anime():
    response = requests.get(f"{BASE_URL}/top/anime")
    return response.json().get("data", [])
