from django.shortcuts import render
from . import db_articles

# Pour avoir accès à la variable article du fichier db_article dans la page articles.html, on ajoute un troisième parametre
# à render qui est context et on lui donne comme valeur une clé et une valeur, la clé prend un nom arbitraire mais la valeur
# prend la variable article du fichier db_articles
# Nous faisons ceci dans ce fichier des views parce que à chaque fois qu'on fera appel à cette fonction, on fera aussi
# appel à la variable article, c'est la seul facon de connecter cette page ou cette vue à cette variable
def articles_view(request):
    return render(request, "articles/liste.html", context={'articles_db': db_articles.articles})
