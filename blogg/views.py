from django.shortcuts import render
# from django.views import generic, View
from django.views.generic import ListView, DetailView
from .models import Post


class PostView(ListView):
    """
    View for home page with list of posts
    """
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'base.html'
    paginated_by = 20


class PostDetails(DetailView):
    """
    View for clicking post to see more
    """
    model = Post
    template_name = 'post_details.html'

