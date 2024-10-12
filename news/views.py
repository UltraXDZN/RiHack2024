from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NewsFull


# Get all news articles (GET)
@require_http_methods(['GET'])
def get_news(request):
    # Fetch all news articles from the database
    news_items = NewsFull.objects.all().values('id', 'title', 'description', 'content', 'author__username', 'banner',
                                               'created_at')

    # Convert the QuerySet to a list of dictionaries and return it as JSON
    return JsonResponse({'news': list(news_items)}, status=200)


# Get a single news article (GET)
@require_http_methods(['GET'])
def get_news_detail(request, news_id):
    try:
        news = NewsFull.objects.values('id', 'title', 'description', 'content', 'author__username', 'banner', 'created_at').get(
            id=news_id)
        return JsonResponse({'news': news}, status=200)
    except NewsFull.DoesNotExist:
        return JsonResponse({'error': 'News not found'}, status=404)


# Create a new news article (POST)
@csrf_exempt  # Only if you're not using CSRF tokens
@require_http_methods(['POST'])
def create_news(request):
    try:
        # Parse the request body for JSON data
        data = json.loads(request.body.decode('utf-8'))

        # Create a new News object
        news = NewsFull.objects.create(
            title=data['title'],
            description=data['description'],
            content=data['content'],
            author=request.user,  # Assuming logged-in user is the author
        )
        return JsonResponse({'success': 'News created successfully', 'news_id': news.id}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)


# Delete a news article (DELETE)
@csrf_exempt  # Only if you're not using CSRF tokens
@require_http_methods(['DELETE'])
def delete_news(request, news_id):
    try:
        news = NewsFull.objects.get(id=news_id)
        news.delete()
        return JsonResponse({'success': 'News deleted successfully'}, status=200)
    except NewsFull.DoesNotExist:
        return JsonResponse({'error': 'News not found'}, status=404)
