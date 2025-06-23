# Fetch and display a webpage’s content

import requests

response = requests.get("https://google.com")
print("Status Code:", response.status_code)
print("Content:\n", response.text)
