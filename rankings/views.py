from django.shortcuts import render

from .controllers import ScoresController, PopulateController
from .models import GameMatch, GameMatchResult, Player, Game



def split_list_columns(l, num_column):
    l_rows = []
    row = []
    elem_count = 0
    for e in l:
        if elem_count < num_column:
            row.append(e)
            elem_count += 1
        else:
            l_rows.append(row)
            row = [e]
            elem_count = 1

    if elem_count != 1:
        l_rows.append(row)

    return l_rows


def populate(request):
    """
    Just to Populate the Database
    """
    populate_controller = PopulateController()
    populate_controller.populate_games()


def index(request):
    """
    View function for home page of site.
    """
    # call controller
    score_controller = ScoresController()
    score_controller.generate_score_points()

    classifications = score_controller.generate_total_classification()

    # Render the HTML template index.html with the data in the context variable
    context = {
        'classifications': classifications,
    }

    return render(request, 'classification.html', context=context)


def matches(request):
    """
    View function for game matches.
    """
    game_matches = GameMatch.objects.filter()
    return render(request, 'matches.html', context={'matches': game_matches})


def matches_details(request, match_id):
    """
    View Function for Game Match Details
    :param match_id:
    :param request:
    :return:
    """

    match = GameMatch.objects.filter(match_id=match_id).first()
    match_results = GameMatchResult.objects.filter(result_match_id=match)

    context = {
        'match_results': match_results,
        'game': match.match_game,
        'match_id': match_id
    }

    return render(request, 'matches_detail.html', context=context)


def players(request):
    """
    View function for display List of Players.
    :param requests:
    :return:
    """
    players = Player.objects.filter()

    players_rows = split_list_columns(players, 2)

    context = {
        'players': players_rows,
    }

    return render(request, 'players.html', context=context)


def player(request, player_nickname):
    """
    View function for display a Player detail.
    :param request:
    :param player_id:
    :return:
    """

    player = Player.objects.filter(player_nickname=player_nickname).first()

    context = {'player': player}

    return render(request, 'player.html', context=context)


def games(request):
    """
    View function for display Games.
    :param request:
    :param game_name:
    :return:
    """

    games = Game.objects.filter()
    games_rows = split_list_columns(games, 2)

    context = {'games_rows': games_rows}

    return render(request, 'games.html', context=context)

def game(request, game_name):
    """
    View function for display Game detail.
    :param request:
    :param game_name:
    :return:
    """

    game = Game.objects.filter(game_name=game_name).first()
    context = {'game': game}

    return render(request, 'game.html', context=context)