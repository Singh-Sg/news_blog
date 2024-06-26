# Generated by Django 3.2.25 on 2024-03-20 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('country', models.CharField(default='in', max_length=50)),
                ('language', models.CharField(default='en', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('news_url', models.URLField(blank=True, null=True)),
                ('urlToImage', models.URLField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('search_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_articles', to='news.searchterm')),
            ],
        ),
    ]
