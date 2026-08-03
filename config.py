import os

# ===== Telegram =====
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ===== Rahavard =====
BASE_URL = "https://rahavard365.com/api/v2"

HEADERS = {
    "application-name": "rahavard",
    "platform": "web",
    "page-id": "33",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "authorization": f"Bearer {os.environ.get('RAHAVARD_TOKEN')}"
}
