import requests

response = requests.get("https://www.google.com")
response.raise_for_status()

print(response.text)
