from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.PasswordInput()
