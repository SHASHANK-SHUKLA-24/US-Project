import requests

url = "https://example.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    with open("downloaded_file.zip", "wb") as f:
        f.write(response.content)
