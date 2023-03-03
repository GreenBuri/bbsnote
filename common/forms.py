#회원가입 기능 추가하지
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta: #메타는 꼭 있어야 한다.
        model = User
        fields = ("username", "email")