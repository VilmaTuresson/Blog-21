from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Post model class
    """
    title = models.CharField(max_length=200)
    post_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post_img = CloudinaryField('image', blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Post model meta class for ordering
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def num_of_likes(self):
        """
        Function to return counted likes
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Comment model class
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        """
        Comment model meta class for ordering
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
