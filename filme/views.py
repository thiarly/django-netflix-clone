# url - view - template

from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

# url - view - template
def homefilmes(request):
    return render(request, 'homefilmes.html')
