release: python manage.py migrate --no-input
web: gunicorn ubook_backend.wsgi 
worker: celery -A ubook_backend worker -l INFO