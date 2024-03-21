## Introduction
The projects aims to fetch news from the newsapi periodically.


### `news/models.py`

This file defines the data models for storing search terms and news articles in the database.

- **SearchTerm**: Represents search terms used to retrieve news articles.
- **News**: Represents news articles.

### `news/task.py`

This file contains tasks to insert retrieved news articles into the database using Celery.

- **insert_data_into_table(article_data, query)**: Inserts news articles into the database if they do not already exist.
- **retrieve_and_insert_news(query, method)**: Retrieves news articles using the specified method and inserts them into the database.
- **find_news_everything()**: Celery task to find and insert all news articles based on search terms.
- **find_top_headlines()**: Celery task to find and insert top headlines based on search terms.

### `news/views.py`

This file contains API views to trigger Celery tasks for retrieving and inserting news articles.

- **trigger_celery_task(request)**: API endpoint to trigger Celery tasks for retrieving and inserting news articles.

### `news/utils.py`

This file contains a class `NewsManager` to interact with the News API and retrieve news articles.

- **NewsManager**:
  - Represents a manager to interact with the News API.
  - **Methods**:
    - `get_everything()`: Retrieves news articles based on the search query parameter.
    - `get_top_headlines(country)`: Retrieves top headlines based on the search query parameter and country.

### `new_filer/celery.py`

This file configures Celery for the Django project.

- Sets the default Django settings module.
- Configures Celery with Django settings and autodiscovers tasks.

### `new_filer/settings.py`
```python
# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BEAT_SCHEDULE = {
    'run-every-morning': {
        'task': 'news.tasks.find_news_everything',
        'schedule': crontab(hour=0, minute=0),  # Run every day at midnight
    },

    'run-every-morning_top_news': {
        'task': 'news.tasks.find_top_headlines',
        'schedule': crontab(hour=0, minute=0),  # Run every day at midnight
    },
}
```
## Run the commands in local
```
sudo apt install celery
```

## Steps to run the app
Run celery worker
```
celery -A new_filer worker -l INFO
```
Run celery beat
```
celery -A new_filer beat -l info
```

## Build the Docker image and start the container:
```
docker-compose up --build
```