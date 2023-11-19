from top200_solo.text_processing import game_matcher


def test_basic_match():
    matched_game = game_matcher.match("17- The Shores of Tripoli")
    assert matched_game == 237860
