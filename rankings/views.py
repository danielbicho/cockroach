from django.shortcuts import render
from django.http import HttpResponseRedirect

from .controllers import ScoresController, PopulateController
from .models import GameMatch, GameMatchResult, Player, Game, Competition, PlayerGameElo, PlayerGeneralElo
from .ops.generate_elo_ratings import game_elo_calculator, general_elo_calculator
from .forms import AddMatchResult


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

    l_rows.append(row)

    return l_rows


def populate(request):
    """
    Just to Populate the Database
    """
    populate_controller = PopulateController()
    populate_controller.populate_games()


# TODO refactor this so it does not always recalculate everything, will be problematic with a bigger set of data
def index(request, competition_id=2):
    """
    View function for home page of site.
    """

    # call controller
    score_controller = ScoresController()
    score_controller.generate_score_points()

    classifications = score_controller.generate_total_classification(competition_id)
    competition_name = Competition.objects.filter(competition_id=competition_id).first().competition_name

    # generate elo
    # TODO Always rebuilding the elo, change this to only update when a game_match is inserted (need a diferent interface from the django admin one)

    for elo in PlayerGameElo.objects.all():
        elo.score = 1500
        elo.save()

    for elo in PlayerGeneralElo.objects.all():
        elo.score = 1500
        elo.save()

    for game_match in GameMatch.objects.filter().all():
        game_elo_calculator(game_match)
        general_elo_calculator(game_match)

    classifications_elo_tuple = []

    for item in classifications:
        player_general_elo = PlayerGeneralElo.objects.filter(player=item.player).first()
        classifications_elo_tuple.append((item, player_general_elo))

    # Render the HTML template index.html with the data in the context variable
    context = {
        'classifications': classifications_elo_tuple,
        'competition_name': competition_name,
    }

    return render(request, 'classification.html', context=context)


# TODO replace all competition_id defaults by CURRENT_COMPETIION GLOBAL VARIABLE
def game_standings(request, game_name, competition_id=1):
    """
    View function for standings by game.

    :param request:
    :param game_name:
    :return:
    """

    score_controller = ScoresController()
    classifications = score_controller.generate_game_standings(game_name, competition_id)
    classifications_elo_tuple = []

    for item in classifications:
        player_game_elo = PlayerGameElo.objects.filter(game=Game.objects.filter(game_name=game_name).filter().first(),
                                                       player=item.player).first()
        classifications_elo_tuple.append((item, player_game_elo))

    context = {
        # 'classifications': classifications,
        'classifications_elo_tuple': classifications_elo_tuple,
        'game_name': game_name,
        'competition_id': competition_id
    }

    return render(request, 'classification_by_game.html', context=context)


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
    :param request:\
    :param player_id:
    :return:
    """

    player = Player.objects.filter(player_nickname=player_nickname).first()
    matches = GameMatch.objects.filter(match_players__player_nickname=player_nickname)

    context = {
        'player': player,
        'matches': matches
    }

    return render(request, 'player.html', context=context)


def games(request):
    """
    View function for display Games.
    :param request:
    :param game_name:
    :return:
    """

    games = Game.objects.filter()
    games_rows = split_list_columns(games[::-1], 2)

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


def competitions(request):
    """

    View function for display Game detail.
    :param request:
    :return:
    """

    return render(request, 'competitions.html')


def add_match_result(request):
    """

    :param request:
    :return:
    """

    if request.method == 'POST':
        form = AddMatchResult(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = AddMatchResult()

    return render(request, 'add_match_result.html', {'form': form})