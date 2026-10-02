import requests
import pandas as pd
from io import StringIO
import time
import json

PHISHTANK_URL = "http://data.phishtank.com/data/online-valid.csv"
OUTPUT_FILE = "phishing_data.csv"

UPDATE_INTERVAL = 3600  # 1 hour


def download_phishtank_data():
    print("Downloading PhishTank data...")

    response = requests.get(PHISHTANK_URL, timeout=30)
    response.raise_for_status()

    data = pd.read_csv(StringIO(response.text))

    data = data[["phish_id", "url", "target"]]

    data.to_csv(OUTPUT_FILE, index=False)

    url_targets = dict(
        zip(
            data["url"].astype(str).str.strip(),
            data["target"].fillna("Unknown")
        )
    )

    with open(
        "extension/url_targets.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            url_targets,
            file,
            indent=2
        )

    print("Download completed.")
    print(f"Total phishing URLs: {len(data)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    while True:

        try:
            download_phishtank_data()

        except Exception as error:
            print(
                f"Update failed: {error}"
            )

        print(
            "Next update in 1 hour..."
        )

        time.sleep(
            UPDATE_INTERVAL
        )