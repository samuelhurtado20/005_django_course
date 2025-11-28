# 005_django_course

Minimal README for the Django course repository.

## Overview
Small Django project used for learning and exercises. Contains app scaffolding, basic views, and tests.

## Requirements
- Python 3.8+
- pip
- virtualenv (recommended)
- (optional) PostgreSQL or other DB if configured

## Setup (Windows)
```powershell
cd /c/Users/developer/source/repos/005_django_course
python -m venv .venv
.venv\Scripts\Activate.ps1    # or .venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Environment
Create a `.env` (or set environment variables) with at least:
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Database
```bash
python manage.py migrate
python manage.py createsuperuser   # optional
```

## Run
```bash
python manage.py runserver
# or to expose on LAN:
python manage.py runserver 0.0.0.0:8000
```

## Tests
```bash
python manage.py test
```

## Project layout
- manage.py
- project_name/       # Django project settings
- app_name/           # example app(s)
- requirements.txt
- README.md

## Contributing
- Create feature branches
- Keep changes small and focused
- Run tests before submitting PRs

## License
Add a LICENSE file for the chosen license. Default: MIT (if applicable).