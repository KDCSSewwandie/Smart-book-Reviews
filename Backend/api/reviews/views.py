from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Review
import urllib.parse
import json

@csrf_exempt
def reviews(request):
    if request.method == 'GET':
        # Retrieve all reviews
        reviews = Review.objects.all().order_by('-date_added').values(
            'id', 'title', 'author', 'rating', 'review_text', 'date_added'
        )
        return JsonResponse({'reviews': list(reviews)}, safe=False)

    elif request.method == 'POST':
        try:
            # Ensure the body is not empty
            if not request.body:
                return JsonResponse({'error': 'Request body is empty'}, status=400)
            
            # Decode the byte string to a regular string
            url_encoded_str = request.body.decode('utf-8')
            
            data = json.loads(url_encoded_str)
            
            review = Review.objects.create(
                title=data['title'],
                author=data['author'],
                rating=data['rating'],
                review_text=data['review'],
            )
            return JsonResponse({'id': review.id, 'message': 'Review created successfully.'}, status=201)
            #return JsonResponse({'id': 'id', 'message': 'Review created successfully.'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Missing required fields.'}, status=400)

@csrf_exempt
def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'PUT':
        # Update an existing review
        try:
            data = json.loads(request.body)
            review.title = data.get('title', review.title)
            review.author = data.get('author', review.author)
            review.rating = data.get('rating', review.rating)
            review.review_text = data.get('review_text', review.review_text)
            review.save()
            return JsonResponse({'message': 'Review updated successfully.'})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)

    elif request.method == 'DELETE':
        # Delete a specific review
        review.delete()
        return JsonResponse({'message': 'Review deleted successfully.'})

    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)