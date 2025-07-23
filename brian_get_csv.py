import os
import requests

def fetch_csv_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    response = requests.get(url)
    if response.ok:
        with open("data/sample_data.csv", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("CSV data saved.")
    else:
        print("Failed to fetch CSV data.")

    if __name__ == "__main__":
        fetch_csv_data()