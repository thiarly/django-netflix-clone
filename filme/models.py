from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISE", "Análise"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTAÇÃO", "Apresentação"),
    ("OUTROS", "Outros"),

)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1500)
    categoria = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    quantidade_views = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
        
    # - Filmes/Séries
    # - thumb
    # - titulo
    # - descrição
    # - categoria
    # - quantidade de views
    # - data da criação
    # - Episodio
    #     - videos
    #     - titulo
# criar os episódios

# criar o usuário