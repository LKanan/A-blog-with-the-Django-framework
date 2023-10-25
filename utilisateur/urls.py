from django.urls import path
from . import views

urlpatterns = [
    path('', views.utilisateurs_view, name='utilisateurs'),
    # Et donc pour utiliser ce chemin on fera adresse_IP/utilisateurs/creer
    path('creer/', views.creer_view, name='creer')
]
