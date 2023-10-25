# HttpResponse est une classe de django qui va nous permettre de retourner une reponse Http à une requette de l'utilisateur
from django.http import HttpResponse
# render est une methode qui va nous aider à retourner notre fichier html comme reponse d'une requette
from django.shortcuts import render

# request est un parametre qui va contenir des informations par rapport à notre requette
# Et ce mode de création de vues n'a pas besoins de fichier html qu'on va renvoyé
def home(request):
    return HttpResponse('Hello Word !')

def contact(request):
    return HttpResponse('Contactez nous au ...')

# Ce mode de création de vue va faire appel aux templates html deja crées
# pour que ces fichiers templates soient reconnu dans le projet python il faut que le dossiers de templetes qui le
# comprend soit spécifier dans le fichier settings
def home_view(request):
    return render(request, "home.html")

def contact_view(request):
    return render(request, "contact.html")

def articles_views(request):
    return render(request,"articles.html")
