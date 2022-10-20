from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=100)
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, models.CASCADE)
    usuario_comentario = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default= timezone.now)
    publicado_comentario = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.nome_comentario