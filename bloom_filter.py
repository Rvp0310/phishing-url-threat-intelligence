import pandas as pd
from pybloom_live import BloomFilter


CSV_FILE = "phishing_data.csv"


def create_bloom_filter():
    print("Loading phishing URLs...")

    data = pd.read_csv(CSV_FILE)

    urls = data["url"].dropna().drop_duplicates()

    print(f"URLs loaded: {len(urls)}")

    bloom = BloomFilter(
        capacity=len(urls),
        error_rate=0.001
    )

    exact_urls = set()

    for url in urls:
        url = str(url).strip()

        bloom.add(url)
        exact_urls.add(url)


    print("Bloom Filter created successfully.")

    return bloom, exact_urls


def check_phishing_url(bloom, exact_urls, url):
    url = url.strip()

    if url not in bloom:
        return False

    if url in exact_urls:
        return True

    return False


if __name__ == "__main__":

    bloom, exact_urls = create_bloom_filter()

    print("\nEnter a URL to check.")
    url = input("URL: ").strip()

    if check_phishing_url(bloom, exact_urls, url):
        print("Phishing URL detected!")
    else:
        print("URL not found in phishing dataset.")