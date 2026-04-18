# Internal Linking Tool (SEO AI Tool)

A Django web application that analyzes blog content and suggests professional internal linking opportunities with anchor text, placement, and SEO reasoning.

## Features
- Paste full blog content into a large text area
- Optional comma-separated target keywords
- AI-powered analysis using OpenAI
- Structured suggestions with anchor text, suggested link topic, placement, and reason
- Copy suggestion button for each card
- Export suggestions to a `.txt` file
- Highlight suggested sentences in the original content
- Save analysis history in SQLite

## Project Structure
- `internal_link_tool/` - Django project settings
- `seo/` - app for SEO analysis
- `templates/seo/index.html` - landing page and results UI
- `static/seo/js/main.js` - copy/export functionality
- `.env` - environment variables and API key
- `requirements.txt` - Python dependencies

## Setup Instructions
1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run database migrations:

```powershell
python manage.py migrate
```

5. Start the development server:

```powershell
python manage.py runserver
```

6. Open the app in your browser at `http://127.0.0.1:8000/`.

## Notes
- The `.env` file is already configured with the OpenAI API key and debug settings.
- If you want to use your own key, update `OPENAI_API_KEY` in `.env`.
- Admin interface is available at `/admin/` after creating a superuser.

## Optional
- Create a superuser:

```powershell
python manage.py createsuperuser
```

- View analysis history in Django admin.
