from django.urls import path
from .views import games_hub_view
from .views import dice_roller_view, ro_sham_po_view

urlpatterns = [
    path('dice-roller/', dice_roller_view, name='dice_rollerURL'),
    path('games-hub/', games_hub_view, name='games_hubURL'),
    path('ro-sham-po/', ro_sham_po_view, name="ro_sham_poURL"),
]
