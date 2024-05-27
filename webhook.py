import requests
import json


def webhook(event_type, data):
    webhook_url = "http://localhost:8000/confluence-webhook"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(data)
    response = requests.post(webhook_url, headers=headers, data=payload)
    if response.status_code != 200:
        print(f"Веб-хук не отправлен: {response.text}")
    else:
        print("Веб-хук отправлен")

    with open('webhook_data.txt', 'a') as f:
        f.write(f"{payload}\n")

data = {
    "repository": {
        "id": 123,
        "name": "test-repo",
        "cloneUrl": "https://github.com/sofiiila/fastapi"
    },
    "commits": [
        {
            "id": "abc123",
            "message": "Initial commit",
            "author": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }
    ]
}

webhook("push", data)
