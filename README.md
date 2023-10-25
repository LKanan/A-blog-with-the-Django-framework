Ceci est un exercice dans la formation du framework Django du langage python pour le web, cet exercice à consisté à la 
création d'un mini site web, et en particulier à la création de deux applications Django dont : articles et utilisateurs,
la gestion des urls, la gestion des vues, la notion des templates, le passage en revu des dossiers qui composent un 
projet Django.
Pour lancer le projet, on doit ouvrir un terminal et s'assurer d'etre dans le dossier qui comprend le projet( le dossier
qui comprend le fichier manage.py et les dossiers articles, utilisateur et Blog ) et puis on lance le server avec la 
commande python manage.py runserver ou python3 manage.py runserver sur un système linux qvec pyton3, cette commande va 
lancer le serveur interne de django avec l'adresse IP http://127.0.0.1:8000/, les urls disponibles sont:
 - /
 - /contact/
et les urls des applications commencent par
 - /utilisateurs/ et 
 - /articles/
Ex: http://127.0.0.1:8000/utilisateurs/ on fait ceci dans un navigateur pour voir le resultat apres avoir lancer le 
server Django

Dans ce projet il n'ya pas eu usage de la base de donnée.