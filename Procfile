web: python manage.py collectstatic --no-input
web: gunicorn kufarbg_app.wsgi
release: python manage.py migrate