import requests

api_key = "790e823db3ee42d58dff47ad06243da7"
url  = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-15&sortBy=publishedAt&apiKey=790e823db3ee42d58dff47ad06243da7"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])