import imp
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostIndex.as_view(), name="index"),
    path('post_categoria/<str:categoria>', views.PostCategoria.as_view(), name="post_categoria"),
    path('post_busca/', views.PostBusca.as_view(), name="post_busca"),
    path('post_detalhes/<int:pk>', views.PostDetalhes.as_view(), name="post_detalhes"),
]