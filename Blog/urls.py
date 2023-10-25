# admin est un module qui va nous permettre d'avoir des outils d'administration qui vont nouspermettre de gerer notre site
from django.contrib import admin
# path est le module qu'on utilise pour définir des chemins
# include est un module qui va nous permettre d'importer des urls vernant des nos différentes applications
from django.urls import path, include

# views est notre fichier qui va contenir nos vues (fonctions)
from . import views

urlpatterns = [
    # path est composé premierement d'un chemin vers une vue, et en duexième parametre on a la fonction qui sera executé
    # lorsqu'on va visiter le chemin en premier parametre, sans oublier ques les vues ce sont des fonction pour django
    path('admin/', admin.site.urls),
    # la chaine de caractères vide à la place du chemin signifie que c'est la reponse lorrqu'on ecrit le l'url par defaut
    # de notre site et donc l'url contenant à la fin le nom de domaine ou l'adresse IP du serveur, ce qui represente la
    # barre apres le l'adresse IP du serveur ou le nom de domaine d'un site (/)
    # Le troisième parametre name de path, bien qu'il ne soit pas obligatoir, il permet quand meme de simplifier le code
    # dans la mesure où on voudrait change le mot qui represente le chemin, par exemple là où on a contact/ on voudrait
    # changer en contactez_nous/, si on fait ca on doit changer dans toutes les page html où on a utilisé ce chemin,
    # alors que s'il y a  un nom, ca nous faciliterai la tache, on pourra seulement changer dans le fichiers des urls mais
    # le nom de l'url restera le meme dans les pages html qui ont utilisé ce lien
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    # Lorsque qu'on fait appelle aux urls venants des applications, leurs chemins sont combinés, genre le chemin donné
    # dans le fichier urls.py de notre application princiapale est celui qui se colle directement après l'adresse IP de notre serveur
    # après ca on ajoute maintenant le chemin créé dans le fichier urls.py de notre l'application créée
    # (le projet) ex: adrees_IP/utilisateurs/url_de_application
    path('utilisateurs/', include('utilisateur.urls')),
    path('articles/', include('articles.urls'))
]
