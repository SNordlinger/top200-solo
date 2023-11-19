from top200_solo.text_processing.game_parser import parser
import logging


def match(input_text):
    log = logging.getLogger()
    res = parser.parse(input_text, debug=log)
    (input, matches) = res
    for match in matches:
        print(f"{match.name} - {match.id}")
    return matches.pop().id
