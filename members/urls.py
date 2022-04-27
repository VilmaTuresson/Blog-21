from django.urls import path
from .views import UserRegistration, UserEditProfile, UpdatePasswordView
from . import views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),
    path('password/', UpdatePasswordView.as_view(template_name='registration/change_passsword.html')),
    path('changed_password', views.changed_password, name='changed_password'),
]
