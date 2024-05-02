from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, required=True)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('gender', 'user_type',)