# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=news_database

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=new_filer.settings

# Set environment variables for Celery
ENV CELERY_BROKER_URL=redis://redis:6379/0
ENV CELERY_RESULT_BACKEND=redis://redis:6379/0

# Set work directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run makemigrations and migrate commands, and create superuser
RUN python manage.py makemigrations news && \
    python manage.py migrate && \
    sh admin-setup.sh

# Expose the port number that the Django development server will listen on
EXPOSE 8000

# Run Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
