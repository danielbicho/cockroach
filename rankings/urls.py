from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matches', views.matches, name='matches'),
    path('matches/<int:match_id>', views.matches_details, name='matches-detail'),
    path('player/<player_nickname>', views.player, name='player'),
    path('players', views.players, name='players'),
    path('game/<game_name>', views.game, name='game'),
    path('games', views.games, name='games')
]