#!/bin/bash

# Create Django superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python manage.py shell
