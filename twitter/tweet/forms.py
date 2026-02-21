from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': "What's happening?",
                'class': 'textarea textarea-bordered textarea-primary w-full bg-slate-800 text-white' 
            }),
            'photo': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered file-input-sm w-full max-w-xs mt-2'
            }),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        