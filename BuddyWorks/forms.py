from django import forms 

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
