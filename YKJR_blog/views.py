from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Specify your template name here
    context_object_name = 'posts'  # Name of the context object to use in the template

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # Specify your template name here
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')  # Redirect to the post list after a successful post creation

    def post_list(request):
        return render(request, 'blog/post_list.html')

    def post_form(request):
        return render(request, 'blog/post_form.html')