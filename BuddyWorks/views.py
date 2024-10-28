from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import LoginForm, SignUpForm

# Create your views here.
def index_view(request):
    return render(request, 'BuddyWorks/index.html')

def role_required(role):
    def decorator(view_func):
        #this user_pass... will fetch the user object and gonna return to lambda
        @user_passes_test(lambda u: u.is_authenticated and u.role == role)
        def _main_func(request, *args, **kwargs):
            return view_func(request, *args,**kwargs)
        return _main_func
    return decorator

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

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("loginURL")
        else:
            messages.error(request, '')
    else:
        form = SignUpForm()

    return render(request, "BuddyWorks/signup.html", {"form":form})
