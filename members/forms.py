from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.contrib.auth.models import User
from django import forms


class RegistrationFields(UserCreationForm):
    """
    Class for additional fields in registration form
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'}))

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    class Meta:
        """
        Meta class for RegistationFields class
        """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        """
        Function to add form control class
        """
        super(RegistrationFields, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    """
    Class for editing profile information
    """
    class Meta:
        """
        Meta class for EditProfileForm class
        """
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class UpdatepasswordForm(PasswordChangeForm):
    """
    Class to update password
    """
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'type': 'password'}))

    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'type': 'password'}))

    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 'type': 'password'}))

    class Meta:
        """
        Meta class for UpdatepasswordForm class
        """
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
