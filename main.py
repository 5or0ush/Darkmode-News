import os, requests, uuid
from flask import Flask, render_template, abort, request, make_response, session
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)  

#NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
NEWSAPI_KEY = "4fe81e4f1271429ea9eed6280388923c"

@app.route("/")
def home():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
        print(f"New session: {session['session_id']}")
    else:
        print(f"Existing session: {session['session_id']}")
    lang = request.args.get("lang", "en")
    search = request.args.get("q", "")
    if not NEWSAPI_KEY:
        abort(500)
    r = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": f"{search} cybersecurity OR security OR breach",
            "language": lang,
            "sortBy": "publishedAt",
            "pageSize": 16,
        },
        headers={"X-Api-Key": NEWSAPI_KEY},
        timeout=10,
    )
    data = r.json()
    articles = data.get("articles", [])
    return render_template("index.html", articles=articles)

@app.route("/track")
def track():
    url = request.args.get("url")
    try:
        with open("resources/visits.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[url] = data.get(url, 0) + 1
    with open("resources/visits.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Tracked click: {url}")
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)