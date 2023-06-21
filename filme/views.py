# url - view - template

from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView

# # Create your views here.
# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'

# # url - view - template
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)
 
class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
     