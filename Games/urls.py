from django.urls import path
from .views import games_hub_view, dice_roller_view

urlpatterns = [
    path('dice-roller/', dice_roller_view, name='dice_rollerURL'),
    path('games-hub/', games_hub_view, name='games_hubURL' )
]
