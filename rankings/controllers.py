import numpy as np

from .models import GameMatchResult, TablePoints, TotalClassification, Player, Game


class PopulateController:

    def populate_matches(self):
        pass

    #def populate_players(self):
    #    player = Player()
    #    player.player_nickname = 'Eversong'
    #    player.player_first_name = 'Daniel'
    #    player.player_last_name = 'Bicho'
    #    player.save()

    def populate_games(self):
        game = Game()
        game.game_complexity = 1.17
        game.game_name = 'Sushi Go'
        game.game_time = 15
        game.game_url = 'https://boardgamegeek.com/boardgame/133473/sushi-go'
        game.save()

        game = Game()
        game.game_complexity = 2.12
        game.game_name = 'Pandemic: Reign of Cthulhu'
        game.game_time = 40
        game.game_url = 'https://www.boardgamegeek.com/boardgame/192153/pandemic-reign-cthulhu'
        game.save()

        game = Game()
        game.game_complexity = 1.03
        game.game_name = 'Dobble'
        game.game_time = 5
        game.game_url = 'https://boardgamegeek.com/boardgame/125048/dobble-free-demo-version'
        game.save()

        game = Game()
        game.game_complexity = 1.67
        game.game_name = 'Dragons & Chickens'
        game.game_time = 20
        game.game_url = 'https://boardgamegeek.com/boardgame/205080/dragons-chickens'
        game.save()

        game = Game()
        game.game_complexity = 1.67
        game.game_name = 'Dragons & Chickens'
        game.game_time = 20
        game.game_url = 'https://boardgamegeek.com/boardgame/205080/dragons-chickens'
        game.save()

        game = Game()
        game.game_complexity = 1.33
        game.game_name = 'Codenames'
        game.game_time = 15
        game.game_url = 'https://boardgamegeek.com/boardgame/178900/codenames'
        game.save()

        game = Game()
        game.game_complexity = 2.35
        game.game_name = 'Catan'
        game.game_time = 120
        game.game_url = 'https://boardgamegeek.com/boardgame/13/catan'
        game.save()

        game = Game()
        game.game_complexity = 3.36
        game.game_name = 'Scythe'
        game.game_time = 115
        game.game_url = 'https://boardgamegeek.com/boardgame/169786/scythe'
        game.save()


class ScoresController:

    def generate_score_points(self):
        game_match_results = GameMatchResult.objects.all()

        for result in game_match_results:
            match = result.result_match_id
            game = match.match_game
            table_points = TablePoints.objects.filter(table_standing=result.result_standing).first()
            if game and table_points:
                result.result_points = table_points.table_score * game.game_complexity
                result.save()

    def generate_total_classification(self):
        classifications = []
        # for player, generate score
        players = Player.objects.all()
        players_score = []
        for player in players:
            score = 0
            game_match_results = GameMatchResult.objects.filter(result_player=player)
            for match in game_match_results:
                score += match.result_points
            players_score.append(score)

        sorted_indexes = np.argsort(players_score)[::-1]

        for i in range(len(sorted_indexes)):
            classification = TotalClassification()
            classification.player = players[int(sorted_indexes[i])]
            classification.standing_position = i + 1
            classification.score_points = round(players_score[int(sorted_indexes[i])], 2)
            classification.save()
            classifications.append(classification)

        return classifications
