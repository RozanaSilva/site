from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def servicojogos_app (request):
    return render (request, 'game_grid.html')

def jogo(request):
    return render(request, 'ttt_pxm.html')

def jogo2(request):
    return render(request, 'ttt_pxp.html')



