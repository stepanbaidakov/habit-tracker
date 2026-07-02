import requests
import os
from dotenv import load_dotenv
from django_celery_beat.models import PeriodicTask, IntervalSchedule

load_dotenv()


def send_message(chat_id, text):
    api_key = os.getenv("API_KEY")
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    try:
        response = requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Telegram error: {e}")
