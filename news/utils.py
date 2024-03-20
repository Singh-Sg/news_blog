from newsapi import NewsApiClient
import json

class NewsManager:
    """
    Class to interact with the News API and retrieve news articles.
    """

    def __init__(self, param, language):
        """
        Initialize the NewsManager object with search parameters.
        
        Args:
            param (str): The search query parameter.
            language (str): The language for the news articles.
        """
        self.param = param
        self.language = language
        self.news_api = NewsApiClient(api_key='c36a7cfa9de346bd912baba6c74e22de')

    def get_everything(self):
        """
        Retrieve news articles based on the search query parameter.

        Returns:
            str: JSON representation of the retrieved news articles.
        """
        try:
            all_articles = self.news_api.get_everything(q=self.param, language=self.language)
            # Check if 'articles' key exists in the response
            if 'articles' in all_articles:
                return json.dumps(all_articles['articles'])
            else:
                return json.dumps([])  # Return empty list if no articles found
        except Exception as e:
            # Log the error and return empty list
            print(f"Error retrieving news articles: {e}")
            return json.dumps([])

    def get_top_headlines(self, country):
        """
        Retrieve top headlines based on the search query parameter and country.

        Args:
            country (str): The country for which to retrieve top headlines.

        Returns:
            str: JSON representation of the retrieved top headlines.
        """
        try:
            top_headlines = self.news_api.get_top_headlines(q=self.param, language=self.language, country=country)
            # Check if 'articles' key exists in the response
            if 'articles' in top_headlines:
                return json.dumps(top_headlines['articles'])
            else:
                return json.dumps([])  # Return empty list if no articles found
        except Exception as e:
            # Log the error and return empty list
            print(f"Error retrieving top headlines: {e}")
            return json.dumps([])
