# url - view - template

from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin



# # Create your views here.
# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'

    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario está logado:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) #redireciona para homepage.html


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # object_list -> lista de objetos do model Filme


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
    # object -> objeto do model Filme
    
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.quantidade_views += 1
        filme.save()
        usuario= request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) #retorna o get da classe pai
     
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None