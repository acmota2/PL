from ply import lex

tokens = [
    'ID',
    'SEP',
    'UINT',
    'DOUBLE',
]

literals = [';', '-', ':']

t_ignore = '\t '

t_ignore_comment = r'\#.*'

t_UINT = r'\d+'

def t_DOUBLE(t): 
   r'\d*\.\d+'
   return t

t_SEP = r'::'

t_ID = r'[_a-zA-Z]\w*'

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print(
        f'Invalid char sequence at line {t.lexer.lineno}: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()
