import itertools
from collections import defaultdict

from ..elo import elo, expected
from ..models import GameMatch, GameMatchResult, PlayerGameElo


def game_elo_calculator(game_match):
    players_game_elo = []
    exp_player_dict = defaultdict()
    result = defaultdict()
    score = defaultdict()

    players = list(game_match.match_players.all())

    # get player result order
    for game_result in GameMatchResult.objects.filter(result_match_id=game_match).all():
        result[game_result.result_player] = game_result.result_standing

    # player elo at the match
    for player in players:
        player_game_elo = PlayerGameElo.objects.filter(game=game_match.match_game, player=player).first()
        if player_game_elo is None:
            player_game_elo = PlayerGameElo()
            player_game_elo.game = game_match.match_game
            player_game_elo.player = player
            player_game_elo.score = 1500
            player_game_elo.save()

        players_game_elo.append(player_game_elo)

    # init structures with 0
    for player in players_game_elo:
        exp_player_dict[player] = 0
        score[player] = 0

    for players_tuple in itertools.combinations(players_game_elo, 2):
        exp_player_dict[players_tuple[0]] += expected(players_tuple[0].score, players_tuple[1].score)
        exp_player_dict[players_tuple[1]] += expected(players_tuple[1].score, players_tuple[0].score)

        if result[players_tuple[0].player] < result[players_tuple[1].player]:
            score[players_tuple[0]] += 1
            score[players_tuple[1]] += 0
        elif result[players_tuple[0].player] == result[players_tuple[1].player]:
            score[players_tuple[0]] += 0.5
            score[players_tuple[1]] += 0.5
        else:
            score[players_tuple[0]] += 0
            score[players_tuple[1]] += 1

    for player_game_elo in players_game_elo:
        new_elo = int(elo(player_game_elo.score, exp_player_dict[player_game_elo], score[player_game_elo]))
        player_game_elo.score = new_elo
        player_game_elo.save()


def general_elo_calculator(players):
    pass


if __name__ == '__main__':
    # TODO make logs of this shit
    for game_match in GameMatch.objects.all():
        game_match = game_match.match_game
        game_elo_calculator(game_match)
