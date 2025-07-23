import os
import requests

def fetch_text_data():
    url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
    response = requests.get(url)
    if response.ok:
        with open("data/sample_text.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Text data saved.")
    else:
        print("Failed to fetch text data.")

if __name__ == "__main__":
    fetch_text_data()
