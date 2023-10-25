# admin est un module qui va nous permettre d'avoir des outils d'administration qui vont nouspermettre de gerer notre site
from django.contrib import admin
# path est le module qu'on utilise pour définir des chemins
from django.urls import path

from . import views

urlpatterns = [
    # path est composé premierement d'un chemin vers une vue, et en duexième parametre on a la fonction qui sera executé
    # lorsqu'on va visiter le chemin en premier parametre, sans oublier ques les vues ce sont des fonction pour django
    path('admin/', admin.site.urls),
    path('', views.home_view)
]
