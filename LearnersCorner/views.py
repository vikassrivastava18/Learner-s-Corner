from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import SignUpForm
from django.contrib.auth import login, authenticate

def index(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})