#!/bin/bash
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth.models import User
from incidents.models import Category
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
categories = ['Accident', 'Fighting', 'Rioting', 'Theft', 'Fire', 'Other']
for name in categories:
    Category.objects.get_or_create(name=name)
print('Setup complete!')
"
gunicorn incident_backend.wsgi:application
