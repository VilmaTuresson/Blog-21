from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Class for creating new post with form
    """
    class Meta:
        """
        Meta class
        """
        model = Post
        fields = ('title', 'content', 'post_img')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

class CommentForm(forms.ModelForm):
    """
    Class for adding a comment to a post
    """
    class Meta:
        """
        Meta class
        """
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

