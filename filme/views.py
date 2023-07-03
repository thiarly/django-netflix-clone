# url - view - template

from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

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
    # object_list -> lista de objetos do model Filme


class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
    # object -> objeto do model Filme
     
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    