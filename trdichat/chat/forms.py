from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Mr.'),
        ('F', 'Miss'),
    )
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'gender')
