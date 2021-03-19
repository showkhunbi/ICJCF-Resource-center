from django import forms
from django.contrib.auth.models import User


class NewStudentForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    department = forms.CharField()
    level = forms.CharField()
    phone = forms.CharField(required=False)

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("Username already exists")
        else:
            return username

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("Email already exists")
        else:
            return email

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        if len(password) <= 5:
            raise forms.ValidationError("Password too short")
        else:
            return password

    def clean_password2(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if (password and password2) and password != password2:
            raise forms.ValidationError("Password does not match")
        else:
            return password2
