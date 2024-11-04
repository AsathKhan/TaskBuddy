from django.shortcuts import render

# Create your views here.
def games_hub_view(request):
    return render(request, 'Games/games.html')

def dice_roller_view(request):
    return render(request, 'Games/dice_roller.html')

def ro_sham_po_view(request):
    return render(request, 'Games/Ro_sham_po.html')