# Incident Reporter Backend

Django REST API for the Cordova Incident Reporter app.

## Setup

Install Python 3.12 or newer, then run these commands from the project root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_incidents
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

## API

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `GET /api/categories/`
- `GET /api/incidents/`
- `POST /api/incidents/`
- `GET /api/incidents/?mine=true`
- `GET /api/incidents/?category=<id>`

The Android emulator can reach the backend at:

```text
http://10.0.2.2:8000/api
```

For a physical phone, use your computer's LAN IP address:

```text
http://YOUR-PC-IP:8000/api
```

When you deploy the backend online, replace the app API Server value with the deployed HTTPS API URL.
