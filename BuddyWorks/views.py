from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def index_view(request):
    return render(request, 'BuddyWorks/index.html')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('indexURL')
            else:
                messages.error(request, "Inavlid username or passowrd")
    else:
        form = LoginForm()
    return render(request, 'BuddyWorks/login.html', {'form':form})