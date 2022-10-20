from urllib import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from categorias.models import Categoria

from django.db.models import Q, Count, Case, When


class PostIndex(ListView):
    model = Post    
    template_name = 'index.html'
    paginate_by = 6
    context_object_name = 'posts'
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post= True)
        
        # Fazendo um filtro na consulta
        qs = qs.annotate(            
            numero_comentarios = Count(
                # Caso publicado comentario for verdadeiro então conta 1
                Case(
                    When(comentario__publicado_comentario = True, then= 1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    template_name = 'post_categoria.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        # recebendo o que foi enviando na url
        categoria = self.kwargs.get('categoria', None)
        # fazendo um filtro por categoria
        qs = qs.filter(categoria_post__nome_cat__iexact= categoria)
        return qs



class PostDetalhes(UpdateView):
    pass
