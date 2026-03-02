from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(
        label='Login', 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    
    password = forms.CharField(
        label='Password', 
        max_length=50, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    
    rep_password = forms.CharField(
        label='Repeat password', 
        max_length=50, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

class SignUpForm(forms.Form):
    login = forms.CharField(
        label='Login', 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )