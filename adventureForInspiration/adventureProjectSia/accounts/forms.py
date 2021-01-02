from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from adventureProjectSia.accounts.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     try:
    #         password_validation.validate_password(password, self.instance)
    #     except forms.ValidationError as error:
    #         # 'Invalid password!'
    #         # Method inherited from BaseForm
    #         self.add_error('password', error)
    #     return password


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)