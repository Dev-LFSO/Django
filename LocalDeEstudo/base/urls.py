from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sala/<str:id>', views.sala, name='sala'),
    path('criar-sala/', views.criar_sala, name='criar-sala'),
    path('atualizar-sala/<str:id>', views.atualizar_sala, name='atualizar-sala'),
    path('apagar-sala/<str:id>', views.apagar_sala, name='apagar-sala')
]