from django.urls import path
from . import views
from . views import jogo, jogo2


urlpatterns = [
    path('', views.servicojogos_app, name='servicojogos'), 
    path('ttt_pxm.html', jogo, name='jogo'),
    path('ttt_pxp.html', jogo2, name='jogo2'),
]