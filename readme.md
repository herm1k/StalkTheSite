# Telegram StalkTheSite Website  Monitor

This Python script monitors web pages for changes and notifies you via Telegram if any changes are detected.

## Features

- Monitors multiple web pages for changes
    
- Checks every minute
    
- Sends a notification to a Telegram chat when a change is detected
    
- Stores page hashes to track changes efficiently
    
- Uses `requests` for HTTP requests and `hashlib` for content hashing
    

## Prerequisites

- Python 3.x
    
- A Telegram bot token (get one via BotFather)
    
- Your Telegram chat ID (you can find it using `getUpdates` API)
    

## Installation

1. Clone the repository:
    
    ```
    git clone https://github.com/herm1k/StalkTheSite
    cd telegram-website-monitor
    ```
    
2. Install dependencies:
    
    ```
    pip install requests
    ```
    
3. Configure the script:
    
    - Set `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in the script.
        
    - Add the URLs you want to monitor in the `URLS` list.
        

## Usage

Run the script with:

```
python StalkTheSite.py
```

To keep it running in the background on a Linux server, use:

```
nohup python StalkTheSite.py &
```

## How It Works

1. The script fetches the webpage content.
    
2. It calculates an SHA-256 hash of the page.
    
3. It compares the hash with the previously stored version.
    
4. If the hash changes, a Telegram notification is sent.
    
5. The new hash is stored for future comparisons.
    

## Notes

- The script creates a `hashes` directory to store page hashes.
    
- If a page fails to load, the script will skip it and retry in the next cycle.
    

## License

This project is open-source and licensed under the MIT License.