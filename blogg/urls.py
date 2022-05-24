from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list_view, name='post_list_view'),
    path('article/<int:post_id>', views.post_details, name='post_details'),
    path('post', views.create_post, name='create_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('like/<int:post_id>', views.like_view, name='like_btn'),
    path('liked_posts', views.liked_posts_view, name='liked_posts'),
    path('delete_comment/<pk>', views.delete_comment, name='delete_comment'),
]
