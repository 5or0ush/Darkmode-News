import os, requests
from flask import Flask, render_template, abort

app = Flask(__name__)

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

@app.route("/")
def home():
    if not NEWSAPI_KEY:
        abort(500)
    r = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": "cybersecurity OR security OR breach",
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 12,
        },
        headers={"X-Api-Key": NEWSAPI_KEY},
        timeout=10,
    )
    data = r.json()
    articles = data.get("articles", [])
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)