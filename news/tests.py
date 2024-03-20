from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch
from news.models import SearchTerm, News
from news.utils import NewsManager
from news.tasks import insert_data_into_table


class TestNewsManager(TestCase):

    def test_get_everything(self):
        manager = NewsManager(param='test', language='en')
        with patch('news.utils.NewsApiClient.get_everything') as mock_get_everything:
            mock_get_everything.return_value = {'articles': [{'title': 'Test Article'}]}
            result = manager.get_everything()
            self.assertEqual(result, '[{"title": "Test Article"}]')

    def test_get_everything_empty_response(self):
        manager = NewsManager(param='test', language='en')
        with patch('news.utils.NewsApiClient.get_everything') as mock_get_everything:
            mock_get_everything.return_value = {}
            result = manager.get_everything()
            self.assertEqual(result, '[]')

    def test_get_top_headlines(self):
        manager = NewsManager(param='test', language='en')
        with patch('news.utils.NewsApiClient.get_top_headlines') as mock_get_top_headlines:
            mock_get_top_headlines.return_value = {'articles': [{'title': 'Test Article'}]}
            result = manager.get_top_headlines(country='us')
            self.assertEqual(result, '[{"title": "Test Article"}]')

    def test_get_top_headlines_empty_response(self):
        manager = NewsManager(param='test', language='en')
        with patch('news.utils.NewsApiClient.get_top_headlines') as mock_get_top_headlines:
            mock_get_top_headlines.return_value = {}
            result = manager.get_top_headlines(country='us')
            self.assertEqual(result, '[]')


class TestInsertDataIntoTable(TestCase):

    def setUp(self):
        self.article_data = [{'title': 'Test Article', 'publishedAt': '2024-03-25T10:00:00', 'url': 'http://example.com'}]

    @patch('news.tasks.News.objects.filter')
    @patch('news.tasks.News.objects.get_or_create')
    def test_insert_data_into_table(self, mock_get_or_create, mock_filter):
        mock_filter.return_value = False  # News article does not exist
        insert_data_into_table(self.article_data, query=1)
        mock_get_or_create.assert_called_once_with(
            search_term_id=1,
            title='Test Article',
            published_at='2024-03-25T10:00:00',
            news_url='http://example.com'
        )

class NewsModelTests(TestCase):

    def test_news_model_str(self):
        search_term = SearchTerm.objects.create(term='Test')
        news = News.objects.create(search_term=search_term, title='Test Title')
        self.assertEqual(str(news), 'Test-Test Title')
