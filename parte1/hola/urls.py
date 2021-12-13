from django.urls import path
from . import views

urlpatterns =[
    path('', views.hola, name='hola'),
    path('vader/', views.vader, name='vader'),
    path('starwars', views.starwars, name='starwars'),
    path('<str:nombre>/', views.saludo, name='saludo'),
]