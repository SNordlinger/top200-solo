from top200_solo.text_processing.lexer import tokens
import ply.yacc as yacc
from . import bgg_search


def p_entry_num(p):
    "entry : NUMBER part"
    p[0] = p[2]


def p_part_title(p):
    "part : TITLE"
    p[0] = (p[1], bgg_search.find_game(p[1]))


def p_part_paren(p):
    "part : part PARENTHETICAL"
    (prev_title, prev_results) = p[1]
    p[0] = (prev_title + p[2], bgg_search.find_game(prev_title, p[2], prev_results))


def p_error(p):
    print(f"error at token {p.type}")
    parser.errok()


parser = yacc.yacc()
