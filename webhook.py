import requests
import json
import os


def webhook(event_type, data):
    webhook_url = "http://localhost:8000/confluence-webhook"
    headers = {"Content-Type": "application/json"}
    payload = {"event_type": event_type, "data": data}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print(f"Веб-хук не отправлен: {response.text}")
    else:
        print("Веб-хук отправлен")


file_path = "/tmp/test_file.txt"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("Hello, World!")

    webhook("file_created", {"file_path": file_path})
else:
    print("Файл уже существует")