#
#  REconhecedor Léxico para BibTeX
#

import ply.lex as lex

states = [
    ('VALUE', 'exclusive')
]

literals = [',','{','}']

tokens = (
    'TIPOreg',
    'PAL',
    'TEXTO',
    'SEP'
)

t_TIPOreg = r'(?i)@article|@book|@incollection|@inproceedings'

t_PAL = r'[a-zA-Z](\w)*'

def t_SEP(t):
    r'='
    t.lexer.begin('VALUE')
    return t

def t_VALUE_TEXTO(t):
    r'\"[^"]*\"|\{[^}]*\}'
    t.lexer.begin('INITIAL')
    return t
    
t_ANY_ignore = ' \n\t'

def t_ANY_error(t):
    print('Illegal character: %s', t.value[0])

lexer = lex.lex()

#lexer = lex.lex(reflags=re.UNICODE) 
#lexer = lex.lex(reflags=re.IGNORECASE) 

# Reading input
#source = ""
##for linha in sys.stdin:
#f = open("bibtex.txt",encoding="utf-8")
#for linha in f:
#	source += linha
#lexer.input(source)
#tok = lexer.token()
#while tok:
#        print(tok)
#        print("-------------------")
#        tok = lexer.token()
