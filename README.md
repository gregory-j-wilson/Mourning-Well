# Mourning Well

A gentle Django web app offering guided reflection prompts and support
resources for people who are grieving. Public-facing, no login required —
reflections are saved privately to the visitor's browser session.

## Features

- **Guided prompts** organized by stage of grief (early days, processing,
  remembering, moving forward), with a random prompt on the home page.
- **Private journaling** — write responses to any prompt; entries are tied
  to the browser session and gathered on a "My Journal" page.
- **Support resources** — hotlines, organizations, and books, grouped by type.
- **Admin panel** to add or edit prompts and resources.

## Running locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ for the app, and
http://127.0.0.1:8000/admin/ for the admin (user: `admin`, pass: `changeme`).

## Project layout

- `support/models.py` — Prompt, Resource, JournalEntry
- `support/views.py` — page logic
- `support/urls.py` — routes
- `support/templates/support/` — HTML templates
- `support/migrations/0002_seed_data.py` — starter prompts & resources

## Before deploying

- Set `DEBUG = False` and a real `SECRET_KEY` (via environment variable).
- Set `ALLOWED_HOSTS` to your domain.
- Change the admin password.
- Consider a persistent database (Postgres) instead of SQLite.
