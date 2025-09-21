# Darkmode-News

A live cyber news dashboard built with Flask.  
It fetches real-time cybersecurity headlines from the NewsAPI, tracks visits, and displays the most viewed articles with a modern dark UI.

## Features

- **Live News Feed**: pulls the latest cybersecurity articles using NewsAPI.
- **Search Bar**: search articles by keyword.
- **Language Selector**: switch between multiple languages.
- **Most Viewed Section**: visit counts are tracked in `resources/visits.json` and displayed.
- **Responsive Dark Theme**: styled with layered gradients, badges, thumbnails, and hover effects.
- **Click Tracking**: all article clicks are logged with title, description, source, date, and count.

## Project Structure

```
Darkmode-News/
├── main.py                # Flask app, routes, NewsAPI fetch, tracking logic
├── requirements.txt       # Dependencies (Flask, Requests, python-dotenv)
├── templates/
│   └── index.html         # Page layout with articles grid and most viewed
├── static/
│   └── styles.css         # Dark theme styling and responsive design
└── resources/
    └── visits.json        # JSON file storing visit counts and metadata
```

## How It Works

1. **News Fetching**  
   `main.py` calls the NewsAPI `/v2/everything` endpoint with cybersecurity-related keywords.  
   Results are passed into `index.html`.

2. **Rendering**  
   Articles are displayed as cards with title, description, badges for source/date, and optional thumbnail.  
   A search input and language dropdown control what is displayed.

3. **Visit Tracking**  
   When a user clicks a link, the `/track` route logs metadata into `resources/visits.json`.  
   The “Most viewed articles” section is built from this file.

4. **Styling**  
   `static/styles.css` defines a dark modern theme: gradient background, blurred sticky header, responsive grid, card hover effects, and styled controls.

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Darkmode-News.git
   cd Darkmode-News
   ```

2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Set your NewsAPI key:
   ```bash
   export NEWSAPI_KEY="your_api_key_here"
   ```

   Or use a `.env` file:
   ```
   NEWSAPI_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   python main.py
   ```

5. Open in browser:  
   [http://localhost:81](http://localhost:81) (or port 5000 if changed).

## Deployment

On Replit:
- Create a new Python project.
- Paste your code.
- Add `NEWSAPI_KEY` under **Secrets**.
- Run with `app.run(host="0.0.0.0", port=81)`.
- Enable “Always On”.

## Future Improvements

- Admin dashboard to configure keywords, sources, refresh rate.
- Tagging and filtering by topic or region.
- Bookmark / read-later functionality.
- User system with roles.
- Notifications or digests.

---

Built as part of **WEB Project 1 – News Flash**: a hands-on project to learn APIs, Flask, deployment, and product design.

## Submission

- **Flask Project Code**: All source files are included in this repository (`main.py`, `templates/index.html`, `static/styles.css`, `resources/visits.json`, and `requirements.txt`).
- **Explanation**:
  - **How it works**: The Flask app fetches articles from the NewsAPI based on cybersecurity-related keywords and renders them in `index.html`. Each click is tracked via the `/track` route, and the most viewed articles are displayed from `resources/visits.json`.
  - **Features added**: 
    - Multi-language support  
    - Search bar  
    - Dark mode with responsive UI  
    - Most viewed section with badges and thumbnails  
    - Custom gradient logo and modern card design  
  - **Tools used**: Flask, Requests, Jinja2 templates, NewsAPI, JSON storage, HTML/CSS. Used AI tools (ChatGPT) for guidance on code structure, styling, and documentation.