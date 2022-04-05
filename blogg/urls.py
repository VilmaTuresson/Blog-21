from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('article/<int:pk>', views.PostDetails.as_view(), name='post_details')
]