
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('escenarios/', views.escenarios, name='escenarios'),
    path('personajes/', views.personajes, name='personajes'),
    path('contacto/', views.contacto, name='contacto'),
]
