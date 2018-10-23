from django.contrib import admin
from .models import GameMatch, Game, Player, GameMatchResult, TablePoints, Competition, PlayerGameElo, PlayerGeneralElo

# Register your models here.

admin.site.register(Game)
admin.site.register(GameMatch)
admin.site.register(Player)
admin.site.register(GameMatchResult)
admin.site.register(TablePoints)
admin.site.register(Competition)
admin.site.register(PlayerGameElo)
admin.site.register(PlayerGeneralElo)