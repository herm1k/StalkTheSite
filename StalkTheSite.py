import hashlib
import requests
import os
import time

# Telegram configuration
TELEGRAM_BOT_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
TELEGRAM_CHAT_ID = "xxxxxxxxxxxxxxxx"

# List of monitored pages
URLS = [
    "http://page",
    "http://page",
]

CHECK_INTERVAL = 60  # Every minute
HASH_DIR = "hashes"  # Hash directory


def get_page_hash(url):
    """Downloads a webpage and returns its SHA-256 hash."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return hashlib.sha256(response.text.encode()).hexdigest()
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None


def get_hash_file_path(url):
    """Returns the file path for storing the hash of a given page."""
    os.makedirs(HASH_DIR, exist_ok=True)  # Create directory if it doesn't exist
    return os.path.join(HASH_DIR, hashlib.md5(url.encode()).hexdigest() + ".txt")


def load_last_hash(url):
    """Loads the last known hash of the page."""
    hash_file = get_hash_file_path(url)
    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            return f.read().strip()
    return None


def save_hash(url, new_hash):
    """Saves the new hash to a file."""
    with open(get_hash_file_path(url), "w") as f:
        f.write(new_hash)


def send_telegram_message(message):
    """Sends a message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


def main():
    """Main loop - checks for changes every minute."""
    print("Monitoring changes on websites...")
    
    while True:
        for url in URLS:
            print(f"Checking: {url}")
            current_hash = get_page_hash(url)
            if current_hash is None:
                continue

            last_hash = load_last_hash(url)

            if last_hash and current_hash != last_hash:
                print(f"⚠️ Page has changed: {url}")
                send_telegram_message(f"🔔 Page has changed! {url}")

            save_hash(url, current_hash)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
