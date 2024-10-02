from django.urls import path
from .views import PostListView, PostCreateView  # Ensure these imports are correct

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
]