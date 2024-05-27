import requests
import json


def webhook(event_type, data):
    webhook_url = "http://192.168.0.102:8000"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(data)
    response = requests.post(webhook_url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"Веб-хук не отправлен: {response.text}")
    else:
        print("Веб-хук отправлен")




