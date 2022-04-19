from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegistrationFields


class UserRegistration(generic.CreateView):
    """
    View for user registrations
    """
    form_class = RegistrationFields
    template_name = 'registration/register.html'
    success_url = reverse_lazy('post_list_view')


class UserEditProfile(generic.UpdateView):
    """
    View for updating profile
    """
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('post_list_view')

    def get_object(self):
        """
        function to return users profile
        """
        return self.request.user
