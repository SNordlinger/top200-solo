from boardgamegeek import BGGClient, BGGRestrictSearchResultsTo
from thefuzz import fuzz

bgg = BGGClient()


def find_game(game_input, optional_input=""):
    print(game_input + optional_input)
    results = bgg.search(game_input + optional_input)
    return results


def get_data(matches):
    pass
