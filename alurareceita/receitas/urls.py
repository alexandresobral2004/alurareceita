from django.urls import path
from . import views

urlpatterns = [
#seta o caminho para as urls e informa a função na view
#path('pasta',funcao view, name='nome_arq')
path('', views.index,name='index'),
path('receita', views.receita,name='receita')
]
