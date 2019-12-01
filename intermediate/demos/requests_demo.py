import requests

response = requests.get("https://www.made.com")
response.raise_for_status()

print(response.text)
