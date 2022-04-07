from django.shortcuts import render, get_object_or_404
# from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def post_list_view(request):
    """
    View for home page with list of posts
    """
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'base.html', context)


def post_details(request, post_id):
    """
    View for clicking post to see more
    """
    post = get_object_or_404(Post, post_id=post_id)
    context = {
        'post': post
    }
    return render(request, 'post_details.html', context)
