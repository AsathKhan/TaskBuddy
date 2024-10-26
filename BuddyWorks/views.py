from django.shortcuts import render, redirect

# Create your views here.
def index_view(request):
    return render(request, 'BuddyWorks/index.html')

def login_view(request):
    return render(request, 'BuddyWorks/login.html')