import ply.lex as lex

tokens = ("NUMBER", "TITLE", "PARENTHETICAL")


t_NUMBER = r"\W*\d+\W*"
t_TITLE = r"[^0-9(\-+~:,]+"
t_PARENTHETICAL = r"\([^)]*\)?"

lexer = lex.lex()
