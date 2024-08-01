import requests
from retry import retry

@retry(tries=3, delay=2, backoff=2)
def make_request(url):
    response = requests.get(url)
    if response.status_code == 429:  # Rate limit error
        raise Exception("Rate limit error")
    return response

url = "https://api.example.com/data"
try:
    response = make_request(url)
    # Process the response
except Exception as e:
    print(f"Failed to make request: {e}")
