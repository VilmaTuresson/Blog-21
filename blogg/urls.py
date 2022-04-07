from blogg.views import post_list_view, post_details
from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list_view, name='post_list_view'),
    path('article/<int:post_id>', views.post_details, name='post_details'),
]
