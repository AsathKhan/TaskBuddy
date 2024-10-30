from django.urls import path
from django.contrib.auth.views import LogoutView
from BuddyWorks.views import index_view
from .views import login_view, signup_view
from .views import dashboard_view, about_view, privacy_policy_view

urlpatterns=[
    path('', index_view, name="indexURL"),
    path('login/', login_view, name="loginURL"),
    path('logout/', LogoutView.as_view(next_page='indexURL'), name='logoutURL'),
    path('signup/', signup_view, name="signupURL"),
    path('dashboard/', dashboard_view, name="dashboardURL"),
    path('about/', about_view, name='aboutURL'),
    path('policy/', privacy_policy_view, name="privacy_policy.html"),
]