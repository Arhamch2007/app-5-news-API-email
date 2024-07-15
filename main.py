import requests
from send_email import send_email

api_key = "790e823db3ee42d58dff47ad06243da7"
url  = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-15&sortBy=publishedAt&apiKey=790e823db3ee42d58dff47ad06243da7"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body +article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)