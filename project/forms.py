from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
class Contactform(forms.Form):
    fullname= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Fullname"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}))
    content=forms.CharField(widget=forms.Textarea())

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Pasword"}))

class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
    Repeat_Password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
        
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
