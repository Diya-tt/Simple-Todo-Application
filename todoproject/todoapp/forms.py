from django import forms
from django.contrib.auth.models import User
from todoapp.models import TodoModel


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"})
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Usename"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"})
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields=["title","description"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"titile"}),
            "description":forms.TextInput(attrs={"class":"form-control","placeholder":"descripton"})
        }

class TodoEditForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields=['title','description','status']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-controler","placeholder":"Title"}),
            "description":forms.TextInput(attrs={"class":"form-controler","placeholder":"Description"}),
        }