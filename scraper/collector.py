import requests
import time


def collect_data(url):
    try:
        print(f"Fetching: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Explicitly set the encoding to UTF-8
        response.encoding = 'utf-8'
        time.sleep(2)  # Adding a delay to avoid overloading the server

        return response.text
    except requests.RequestException as e:
        print(f"ERROR: Failed to fetch data -> {e}")
        return None
