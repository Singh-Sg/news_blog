## Introduction
The projects aims to fetch news from the newsapi periodically.

## Steps to run the app
Run celery worker
```
celery -A new_filer worker -l INFO
```
Run celery beat
```
celery -A new_filer beat -l info
```