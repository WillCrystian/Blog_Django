from urllib import request
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from comentarios.models import Comentario
from .models import Post
from comentarios.form import ComentarioForm
from django.contrib import messages
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
    template_name = 'post_busca.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        termo = self.request.GET.get('termo')
        
        if not termo:
            return qs
        
        qs = qs.filter(
            Q(titulo_post__icontains = termo) | Q(autor_post__first_name__iexact = termo) |
            Q(conteudo_post__icontains = termo) | Q(excerto_post__icontains = termo) |
            Q(categoria_post__nome_cat__iexact = termo)
        )
        
        return qs


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
    template_name = 'post_detalhes.html'
    model = Post
    # Qual form devo enviar
    form_class = ComentarioForm
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        contexto =  super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado_comentario= True, 
                                                post_comentario= post.id)
        contexto['comentarios'] = comentarios
        
        return contexto
    
    def form_valid(self, form):
        # obtendo post
        post = self.get_object()
        # desempacotando post
        comentario = Comentario(**form.cleaned_data)
        
        comentario.post_comentario = post
        
        # usuario logado adiciona o mesmo 
        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user
            
        comentario.save()
        messages.success(self.request, 'Comentário adicionado com sucesso')
        return redirect('post_detalhes', pk= post.id)
        