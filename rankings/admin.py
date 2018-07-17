from django.contrib import admin
from .models import GameMatch, Game, Player, GameMatchResult, TablePoints

# Register your models here.

admin.site.register(Game)
admin.site.register(GameMatch)
admin.site.register(Player)
admin.site.register(GameMatchResult)
admin.site.register(TablePoints)
