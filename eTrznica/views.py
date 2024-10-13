# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Advertisement
import json


def list_posts(request):
    if request.method == 'GET':
        posts = Advertisement.objects.all().order_by('-created_at')
        posts_list = []
        for post in posts:
            posts_list.append({
                'id': post.id,
                'title': post.title,
                'businessName': post.business_name,
                'content': post.content,
                'city': post.city,
                'imageUrl': post.image.url if post.image else None,
            })
        return JsonResponse({'posts': posts_list})
    else:
        return JsonResponse({'error': 'GET method required'}, status=400)


@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        business_name = request.POST.get('businessName')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        city = request.POST.get('city')
        print(request.POST)

        if not all([title, business_name, content]):
            return JsonResponse({'error': 'Missing fields'}, status=400)

        post = Advertisement(title=title, business_name=business_name, content=content, image=image, city=city)
        post.save()
        return JsonResponse({'message': 'Post created successfully', 'id': post.id})
    else:
        return JsonResponse({'error': 'POST method required'}, status=400)


@csrf_exempt
def edit_post(request, ad_id):
    try:
        post = Advertisement.objects.get(pk=ad_id)
    except Advertisement.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

    if request.method == 'POST':
        title = request.POST.get('title')
        business_name = request.POST.get('businessName')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        city = request.POST.get('city')

        if not all([title, business_name, content]):
            return JsonResponse({'error': 'Missing fields'}, status=400)

        post.title = title
        post.business_name = business_name
        post.content = content
        post.city = city

        if image:
            post.image = image

        post.save()
        return JsonResponse({'message': 'Post updated successfully'})
    else:
        return JsonResponse({'error': 'POST method required'}, status=400)


@csrf_exempt
def delete_post(request, ad_id):
    if request.method == 'POST':
        try:
            post = Advertisement.objects.get(pk=ad_id)
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'})
        except Advertisement.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    else:
        return JsonResponse({'error': 'POST method required'}, status=400)
