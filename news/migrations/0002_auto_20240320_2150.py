# Generated by Django 3.2.25 on 2024-03-20 21:50

from django.db import migrations


def insert_search_terms(apps, schema_editor):
    SearchTerm = apps.get_model('news', 'SearchTerm')
    SearchTerm.objects.create(term='Cricket', country='in', language='en')
    SearchTerm.objects.create(term='Elon Mask', country='us', language='en')


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_search_terms),
    ]
