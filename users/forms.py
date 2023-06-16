from django import forms

from users.models import User


class AuthenticationForms(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('email', 'password')


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    avatar = forms.ImageField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'password')

