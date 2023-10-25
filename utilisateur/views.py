from django.shortcuts import render
from django.http import HttpResponse
def utilisateurs_view(request):
    return HttpResponse("Page d'utilisateurs")

def creer_view(request):
    #On met utilisateurs/liste.html puisque le dossier qui est reconnu est templates et non utilisateurs, alors dans le
    #chemin du fichier html on doit mettre le nom du sous dossier qui le comprend
    return render(request, 'utilisateurs/liste.html')