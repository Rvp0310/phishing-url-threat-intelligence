# Phishing URL Detection and Browser Blocking System

A threat-intelligence based phishing URL detection system that uses
PhishTank data, Bloom Filter, Flask API and a Chrome/Edge browser extension.

## Architecture

PhishTank Feed
      ↓
Web Data Collector
      ↓
Phishing Dataset
      ↓
Bloom Filter + Exact URL Set
      ↓
Flask API
      ↓
Browser Extension
      ↓
URL Detection → Block / Allow

## Technologies Used

- Python
- Pandas
- Bloom Filter
- Flask
- JavaScript
- Chrome/Edge Extension
- PhishTank

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Running the Project

### 1. Start the Crawler

Run the crawler to download the phishing threat-intelligence dataset:

```bash
python crawler.py
```

The crawler updates the local phishing dataset and target mapping.

### 2. Start the Flask API

Run the Flask API:

```bash
python api.py
```

The API runs locally at:

```text
http://127.0.0.1:5000
```

### 3. Load the Browser Extension

1. Open `chrome://extensions/` in Chrome or `edge://extensions/` in Edge.
2. Enable **Developer Mode**.
3. Select **Load unpacked**.
4. Select the project's `extension` folder.
5. Keep the Flask API running.
6. Visit a URL contained in the phishing dataset.

If the URL is detected as phishing, the extension redirects the browser to the blocking page.

## Project Components

### `crawler.py`

Downloads the phishing threat-intelligence dataset and updates the local dataset and target mapping files.

### `bloom_filter.py`

Creates the Bloom Filter and exact URL set used for efficient URL checking.

### `api.py`

Provides the `/check` endpoint used by the browser extension to check URLs.

### `extension/`

Contains the browser extension responsible for monitoring navigation, checking URLs through the Flask API, and redirecting detected phishing URLs to the blocking page.

## Important Note

The browser extension requires the Flask API to be running locally.

The system is intended as an academic/demo project for phishing URL detection and browser-based blocking.
