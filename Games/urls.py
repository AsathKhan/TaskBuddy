from django.urls import path
from Games.views import dice_roller_view

urlpatterns = [
    path('dice-roller/', dice_roller_view, name='dice_rollerURL'),
]
