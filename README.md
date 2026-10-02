# Phishing URL Detection and Browser Blocking System

A threat-intelligence-based phishing URL detection system that uses PhishTank data, a Bloom Filter, a Flask API, and a Chrome/Edge browser extension to detect and block known phishing URLs.

## Architecture

```text
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
URL Detection
    ↙     ↘
 Safe    Phishing
  ↓         ↓
Allow     Block
```

## Technologies Used

* Python
* Pandas
* Bloom Filter
* Flask
* JavaScript
* Chrome/Edge Extension
* PhishTank

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

### 1. Start the Web Data Collector

Run the web data collector:

```bash
python web_crawler.py
```

It downloads the phishing threat-intelligence dataset and updates the local phishing URL data.

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

### `web_crawler.py`

Collects phishing URL data from the threat-intelligence source and updates the local dataset.

### `bloom_filter.py`

Creates the Bloom Filter and exact URL set used for efficient phishing URL checking.

### `api.py`

Provides the `/check` endpoint used by the browser extension to check URLs.

### `target_mapper.py`

Maps detected phishing URLs to their targeted organization or service using the threat-intelligence dataset and provides the target information for the browser blocking page.

### `extension/`

Contains the browser extension responsible for monitoring browser navigation, checking URLs through the Flask API, and redirecting detected phishing URLs to the blocking page.

## Important Note

The browser extension requires the Flask API to be running locally.

The system is intended as an academic/demo project for phishing URL detection and browser-based blocking.
