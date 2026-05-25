import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers
)

print(response.text)
