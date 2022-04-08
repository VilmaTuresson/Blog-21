from django import forms
from .models import Post


class PostForm(forms.Form):
    """
    Class for creating new post with form
    """
    class Meta:
        """
        Meta class
        """
        model = Post
        fields = ('title', 'content', 'post_img')
