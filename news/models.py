from django.db import models

class SearchTerm(models.Model):
    """
    Model to store search terms for retrieving news articles.
    """
    term = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="in")  # Default country is India
    language = models.CharField(max_length=50, default="en")  # Default language is English

    def __str__(self):
        return self.term


class News(models.Model):
    """
    Model to store news articles.
    """
    search_term = models.ForeignKey(SearchTerm, on_delete=models.CASCADE, related_name='news_articles')
    title = models.CharField(max_length=255)
    description = models.TextField()
    source = models.CharField(max_length=100)  # Source of the news article
    author = models.CharField(max_length=255, null=True, blank=True)  # Author of the news article (optional)
    news_url = models.URLField(null=True, blank=True)  # URL of the news article
    urlToImage = models.URLField(null=True, blank=True)  # URL to the image associated with the news article
    content = models.TextField(null=True, blank=True)  # Content of the news article
    published_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the news article was published

    def __str__(self):
        return f"{self.search_term.term}-{self.title}"
