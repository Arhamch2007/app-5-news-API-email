import requests
from send_email import send_email

topic = "tesla"

api_key = "790e823db3ee42d58dff47ad06243da7"
url  = f"https://newsapi.org/v2/everything?q={topic}&from=2024-06-15&sortBy=publishedAt&apiKey=790e823db3ee42d58dff47ad06243da7&language=en"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body +article["title"] + "\n" + article["description"] +"\n" + article["url"]  + 2*"\n"

body = body.encode("utf-8")
send_email(body)