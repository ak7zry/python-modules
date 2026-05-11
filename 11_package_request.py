import requests

# GET request sederhana
respons = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if respons.status_code == 200:
    data = respons.json()
    print("Title:", data["title"])
    print("Body:", data["body"])
else:
    print("Error:", respons.status_code)