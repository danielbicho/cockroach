from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matches', views.matches, name='matches'),
    path('matches/<int:match_id>', views.matches_details, name='matches-detail'),
    path('players/<player_nickname>', views.players, name='players'),
    path('games/<game_name>', views.games, name='games')
]