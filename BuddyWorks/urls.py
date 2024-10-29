from django.urls import path
from BuddyWorks.views import index_view
from .views import login_view, signup_view
from .views import dashboard_view

urlpatterns=[
    path('', index_view, name="indexURL"),
    path('login/', login_view, name="loginURL"),
    path('signup/', signup_view, name="signupURL"),
    path('dashboard/', dashboard_view, name="dashboardURL"),
]