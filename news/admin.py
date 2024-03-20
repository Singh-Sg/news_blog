from django.contrib import admin
from news.models import SearchTerm, News


admin.site.register(News)
admin.site.register(SearchTerm)
