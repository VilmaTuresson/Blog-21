from django.urls import path
from .views import UserRegistration, UserEditProfile

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),
]
