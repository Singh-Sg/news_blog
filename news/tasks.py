from celery import shared_task, Celery
from news.models import News, SearchTerm
from news.utils import NewsManager
import json
import logging

# Configure logging
logger = logging.getLogger(__name__)

app = Celery()

def insert_data_into_table(article_data, query):
    try:
        for news in article_data:
            if not News.objects.filter(title=news['title']):
                news['published_at'] = news.pop('publishedAt')
                news['news_url'] = news.pop('url')
                News.objects.get_or_create(
                    search_term_id=query,
                    **news
                )
                logger.info(f"Inserted news article '{news['title']}' into the database.")
            else:
                logger.debug(f"News article '{news['title']}' already exists in the database. Skipping insertion.")
    except Exception as e:
        # Log the error
        logger.error(f"Error inserting data into table: {e}")


def retrieve_and_insert_news(query, method):
    try:
        logger.debug(f"Retrieving news articles for search term '{query[1]}'...")
        article_data = method
        logger.debug(f"Received news articles: {article_data}")
        insert_data_into_table(json.loads(article_data), query[0])
    except Exception as e:
        # Log the error
        logger.error(f"Error finding news: {e}")


@shared_task
def find_news_everything():
    search_terms = SearchTerm.objects.all().values_list()
    for query in search_terms:
        retrieve_and_insert_news(query, NewsManager(query[1], query[3]).get_everything())


@shared_task
def find_top_headlines():
    search_terms = SearchTerm.objects.all().values_list()
    for query in search_terms:
        retrieve_and_insert_news(query, NewsManager(query[1], query[3]).get_top_headlines(query[2]))
