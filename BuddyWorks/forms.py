from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, 
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'User Name',
                                   'class': 'input-field'
                               }))
                                
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Password',
                                    'class': 'input-field'}),
                               required=True)
    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
