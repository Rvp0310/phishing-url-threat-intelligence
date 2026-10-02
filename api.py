from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from bloom_filter import create_bloom_filter, check_phishing_url

app = Flask(__name__)
CORS(app)

CSV_FILE = "phishing_data.csv"

bloom, exact_urls = create_bloom_filter()

last_modified = os.path.getmtime(CSV_FILE)

def update_if_needed():
    global bloom, exact_urls, last_modified

    current_modified = os.path.getmtime(CSV_FILE)

    if current_modified != last_modified:

        print("New phishing data detected.")
        print("Updating Bloom Filter...")

        bloom, exact_urls = create_bloom_filter()

        last_modified = current_modified

        print("Bloom Filter updated.")

@app.route("/check", methods=["GET"])
def check_url():

    update_if_needed()
    
    url = request.args.get("url")

    if not url:
        return jsonify({
            "error": "No URL provided"
        }), 400

    is_phishing = check_phishing_url(
        bloom,
        exact_urls,
        url
    )

    if is_phishing:
        return jsonify({
            "phishing": True,
            "message": "Phishing URL detected"
        })

    return jsonify({
        "phishing": False,
        "message": "URL not found in phishing dataset"
    })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )