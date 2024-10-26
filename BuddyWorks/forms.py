from django import forms 

class Loginform(forms.Form):
    username = forms.charField(max_length=150, required=True)
    password = forms.charField(widget=forms.PasswordInput, required=True)