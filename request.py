import requests
import json

url = "http://localhost:8000/confluence-webhook"

data = {
    "repository": {
        "cloneUrl": "https://github.com/sofiiila/fastapi"
    }
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())