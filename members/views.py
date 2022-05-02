from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationFields, EditProfileForm, UpdatepasswordForm


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
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('post_list_view')

    def get_object(self):
        """
        function to return users profile
        """
        return self.request.user


class UpdatePasswordView(PasswordChangeView):
    """
    Class for changing password
    """
    form_class = UpdatepasswordForm
    success_url = reverse_lazy('changed_password')


def changed_password(request):
    """
    Function to redirect user if password is changed successfully
    """
    return render(request, 'registration/changed_password.html', {})
