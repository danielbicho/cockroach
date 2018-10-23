from django.db import models


# Create your models here.

class Player(models.Model):
    """
    Model representing a Player.
    """
    player_nickname = models.CharField(max_length=15, primary_key=True, null=False)
    player_first_name = models.CharField(max_length=15, null=False)
    player_last_name = models.CharField(max_length=15, null=False)
    player_photo = models.ImageField()
    player_bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.player_nickname


class Game(models.Model):
    """
    Model representing a Game.
    """
    game_name = models.CharField(max_length=30, primary_key=True)
    game_complexity = models.FloatField()
    game_time = models.IntegerField()
    game_url = models.URLField()
    game_logo = models.ImageField(null=True)

    # genre choices field?

    def __str__(self):
        return self.game_name


class Competition(models.Model):
    """
    Model representing a Competition.
    """

    competition_id = models.IntegerField(primary_key=True)
    competition_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.competition_name


class PlayerGameElo(models.Model):
    """
    Model representing a Player ELO at a specific game.
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(null=False, default=1500)


class PlayerGeneralElo(models.Model):
    """
    Model representing a Player General ELO.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(null=False, default=1500)


class GameMatch(models.Model):
    """
    Model representing a Game Match.
    """
    # game match primary key
    match_id = models.IntegerField()
    match_date = models.DateField('Match Date')
    match_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    match_players = models.ManyToManyField(Player)
    competition_id = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match_id)


class GameMatchResult(models.Model):

    class Meta:
        unique_together = (('result_match_id', 'result_player'),)

    result_match_id = models.ForeignKey(GameMatch, on_delete=models.CASCADE)
    result_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    result_standing = models.IntegerField()
    result_points = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class TablePoints(models.Model):
    table_standing = models.IntegerField()
    table_score = models.IntegerField()


class TotalClassification(models.Model):

    class Meta:
        unique_together = (('standing_position', 'player'),)

    standing_position = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score_points = models.FloatField()
    performance_points = models.FloatField()
    competition_id = models.ForeignKey(Competition, on_delete=models.CASCADE)