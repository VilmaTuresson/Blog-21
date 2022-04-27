from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.views import generic, View
from django.urls import reverse, reverse_lazy
from .models import Post, User, Comment


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
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm(request.POST)

    if request.method == 'POST':
        if comment_form.is_valid():
            post_comment = comment_form.save(commit=False)
            post_comment.name = request.user
            post_comment.post = post
            post_comment.save()
            return redirect(request.path_info)
            
    liked_post = get_object_or_404(Post, post_id=post_id)
    num_of_likes = liked_post.num_of_likes()

    liked = False
    if liked_post.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'post': post,
        'num_of_likes': num_of_likes,
        'liked': liked,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'post_details.html', context)


def like_view(request, post_id):
    """
    View for liking posts
    """
    post = get_object_or_404(Post, post_id=post_id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_details', args=[str(post_id)]))


def create_post(request):
    """
    View for creating new post
    """
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_list_view')
        
    return render(request, 'create_post.html', {'form': form})


def delete_post(request, post_id):
    """
    View for deleting post
    """
    post = get_object_or_404(Post, post_id=post_id)
    if request.user == post.author:
        post.delete()

    return redirect('post_list_view')


def edit_post(request, post_id):
    """
    View for editing post
    """
    post = get_object_or_404(Post, post_id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_list_view')
    form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)


def liked_posts_view(request):
    """
    View for user activity, created and liked posts
    """
    user_id = request.user
    posts = Post.objects.filter(author=user_id)
    user_liked_posts = Post.objects.filter(likes__username__contains=user_id)

    if request.GET:
        if 'liked' in request.GET['userposts']:
            posts = user_liked_posts
            

    context = {
        'posts': posts,
    }

    return render(request, 'liked_posts.html', context)



# class AddCommentView(CreateView):
#     """
#     View for creating comment
#     """
    
#     model = Comment
#     form_class = CommentForm
#     login_required = True
#     template_name = 'add_comment.html'

#     def get_success_url(self):
#         """
#         Function to return to post after commenting
#         """
#         comment_return = self.kwargs['post_id']
#         return reverse_lazy('post_details', kwargs={'post_id': comment_return})

#     def form_valid(self, form):
#         """
#         Function to validate comment form
#         """
#         form.instance.post_id = self.kwargs['post_id']
#         return super().form_valid(form)

@login_required
def delete_comment(request, pk):
    """
    Function to delete comment
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
