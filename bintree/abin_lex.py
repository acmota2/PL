import ply.lex as lex

tokens = (
    'NUM',
    'PAL',
    'VAZIO'
)

literals = ['(',')']

t_NUM = r'\d+'

def t_VAZIO(t):
    r'NULL'
    return t

t_PAL = r'\'[_a-zA-Z]\w*\''

t_ignore = ' \n\t'

def t_error(t):
    print(f'Lexic error with {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()
