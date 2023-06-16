# url - view - template
from django.urls import path, include
from .views import homepage, homefilmes

urlpatterns = [
    path('', homepage),
    path('filmes/', homefilmes),
]