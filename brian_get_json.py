import os
import requests

def fetch_json_data():
    url = "https://api.github.com/repos/python/cpython"
    response = requests.get(url)
    if response.ok:
        with open("data/sample_data.json", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("JSON data saved.")
    else:
        print("Failed to fetch JSON data.")

if __name__ == "__main__":
    fetch_json_data()