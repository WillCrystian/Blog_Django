from django.contrib import admin
from comentarios.models import Comentario

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id','nome_comentario', 'email_comentario','post_comentario',
                    'usuario_comentario', 'data_comentario', 'publicado_comentario')
    list_display_links = ('id', 'nome_comentario')
    list_editable = ('publicado_comentario',)
    
admin.site.register(Comentario, ComentariosAdmin)