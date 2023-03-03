from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST) #UserForm에서 요청 들어온거 다 받은다음에
        if form.is_valid(): #요청 들어온게 POST인거 모두
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})