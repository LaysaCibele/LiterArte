from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:livro_id>/', views.adicionar_na_lista, name='adicionar_na_lista'),
    path('meus-livros/', views.pagina_minha_lista, name='minha_lista'),
]