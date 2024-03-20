from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.tasks import find_top_headlines, find_news_everything


@api_view(['GET'])
def trigger_celery_task(request):
    try:
        find_news_everything.delay()
        find_top_headlines.delay()
        return Response({'message': 'Celery task triggered successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
