import sys
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import ply.yacc as yacc
from bibtex_lex import tokens

def p_bibtex(p):
	'bibtex : referencias'
	p[0] = p[1]

def p_referencias(p):
	"referencias : referencias referencia"
	p[0] = p[1] + 1

def p_referencias_empty(p):
	'referencias : '
	p[0] = 0

def p_bibtex_referencias(p):
	"referencia : TIPOreg '{' PAL ',' campos '}'"
	if p[3] in parser.chaves:
		print(f'Key {p[3]} already in use!')
		parser.success = False
		pass
	else:
		parser.chaves.add(p[3])
		parser.count_correct += 1

def p_grammar_rest(p):
	"""
	campos      : campos ',' campo               
	campos      : campo              
	campo       : PAL SEP  TEXTO                  
	"""

#campos : campo outrosC  # { PAL }
#outrosC : ',' campos     # { , }            
#outrosC : €              # { '}' }

def p_error(p):
    print("Syntax error in input!", p)
    parser.success=False

parser = yacc.yacc()
parser.success=True
parser.chaves = set()
parser.count_correct = 0

source = ""
f = sys.stdin
if len(sys.argv) > 1:
	f = open(sys.argv[1],encoding="utf-8")
for linha in f:
	source += linha

result = parser.parse(source)
if parser.success:
   print('Parsing completed!')
else:
   print('Parsing failed!')
print(f'Counted {parser.count_correct} different references in a total of {result}')
