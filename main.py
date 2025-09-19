import os, requests, uuid
from flask import Flask, render_template, abort, request, make_response, session
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)  

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")




@app.route("/")
def home():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
        print(f"New session: {session['session_id']}")
    else:
        print(f"Existing session: {session['session_id']}")
    lang = request.args.get("lang")
    if lang:
        session["lang"] = lang
    else:
        lang = session.get("lang", "en")
        session["lang"] = lang
    search = request.args.get("q", "")
    if not NEWSAPI_KEY:
        abort(500)
    r = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": f"{search} cybersecurity OR security OR hacker OR cyberattack",
            "language": lang,
            "sortBy": "publishedAt",
            "pageSize": 12,
        },
        headers={"X-Api-Key": NEWSAPI_KEY},
        timeout=10,
    )
    data = r.json()
    articles = data.get("articles", [])
    with open("resources/visits.json", "r") as f:
        visits = json.load(f)
    top_sites = sorted(visits.items(), key=lambda x: x[1]["count"], reverse=True)[:6]

    most_visited = []
    for url, data in top_sites:
        most_visited.append({
            "url": url,
            "count": data["count"],
            "source": data.get("source", "Unknown"),
            "title": data.get("title", url),
            "description": data.get("description", ""),
            "publishedAt": data.get("publishedAt", "")
        })
    return render_template("index.html", articles=articles, most_visited=most_visited)



@app.route("/track")
def track():
    url = request.args.get("url")
    title = request.args.get("title")
    description = request.args.get("description")
    source = request.args.get("source")
    publishedAt = request.args.get("publishedAt")

    try:
        with open("resources/visits.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if url in data:
        data[url]["count"] += 1
    else:
        # new entry with metadata
        data[url] = {
            "count": 1,
            "title": title or url,
            "description": description or "",
            "source": source or "Unknown",
            "publishedAt": publishedAt or ""
        }

    with open("resources/visits.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Tracked click: {url}")
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)