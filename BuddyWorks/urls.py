from django.urls import path
from django.contrib.auth.views import LogoutView
from BuddyWorks.views import index_view
from .views import login_view, signup_view
from .views import dashboard_view, task_overview_view
from .views import privacy_policy_view, terms_of_service_view
from .views import about_view, support_view, service_view

urlpatterns=[
    path('', index_view, name="indexURL"),
    path('login/', login_view, name="loginURL"),
    path('logout/', LogoutView.as_view(next_page='indexURL'), name='logoutURL'),
    path('signup/', signup_view, name="signupURL"),
    path('dashboard/', dashboard_view, name="dashboardURL"),
    path('about/', about_view, name='aboutURL'),
    path('privacy-policy/', privacy_policy_view, name="privacy-policyURL"),
    path('terms-of-service/', terms_of_service_view, name="terms-of-serviceURL"),
    path('support/', support_view, name="supportURL"),
    path('service', service_view, name="serviceURL"),
    path('task-overview/', task_overview_view, name='task-overviewURL'),
]