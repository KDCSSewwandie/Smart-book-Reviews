from django.urls import path
from .views import *

urlpatterns = [
    path('reviews/', reviews, name='reviews'),
    path('reviews/<int:review_id>/', review_detail, name='review_detail'),
]