from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    def clean(self):
        # obtendo os dados dos comentarios
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')
        
        # messagem de erro
        if len(nome) < 2:
            self.add_error('nome_comentario',
                           'Nome precisa ter no mínimo 2 letras')
        
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')