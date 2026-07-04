# Hotel Booking Backend

Backend for a simple hotel reservation system built with Django and Django REST Framework.

## Overview

- Small Django project providing models for `Hotel`, `Room`, and `Reservation`.
- REST API via Django REST Framework viewsets and simple class-based views for templates.

## Tech Stack

- Python 3.x
- Django
- Django REST Framework

## Setup

1. Create a virtual environment and install requirements (Django, djangorestframework).
2. Run migrations: `python manage.py migrate`.
3. Create a superuser if needed: `python manage.py createsuperuser`.
4. Run server: `python manage.py runserver`.

## Notes

- Database: `db.sqlite3` (development).
- Keep `SECRET_KEY` out of source control for production — use environment variables.

## Endpoints (examples)

- `api/hotels/` — list and manage hotels
- `api/rooms/` — list and manage rooms
- `api/reservations/` — create and manage reservations

---
Project prepared for repository import with concise commits and documentation.
