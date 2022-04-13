from blogg.views import post_list_view, post_details, create_post, delete_post, edit_post, like_view
from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list_view, name='post_list_view'),
    path('article/<int:post_id>', views.post_details, name='post_details'),
    path('post', views.create_post, name='create_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('like/<int:post_id>', views.like_view, name='like_btn'),
]
