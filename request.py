import requests
import json

url = "http://192.168.0.102:8000"

data = {
    "repository": {
        "cloneUrl": "https://github.com/sofiiila/fastapi"
    }
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())