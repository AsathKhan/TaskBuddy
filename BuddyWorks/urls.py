from django.urls import path
from BuddyWorks.views import index

urlpatterns=[
    path('', index, name="indexURL"),
]