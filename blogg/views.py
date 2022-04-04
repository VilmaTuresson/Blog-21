from django.shortcuts import render
from django.views import generic
from .models import Post


class PostView(generic.ListView):
    """
    View for home page with list of posts
    """
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'base.html'
    paginated_by = 20
