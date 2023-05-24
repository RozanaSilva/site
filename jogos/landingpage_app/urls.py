from django.urls import include, path

from . import views

app_name = 'landingpage_app'

urlpatterns = [
    path('',  views.landing_page, name= 'landing_page'),
    
]