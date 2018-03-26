from django.urls import path
from . import views

app_name = 'relatedgamesearch'
urlpatterns = [
    # ex: /relategegamesearch/
    path('', views.index, name='index'),
    path('favoritegame/', views.get_favorite_game_name, name='favoritegame'),
]