import json
import sys
import ply.yacc as yacc
from abin_lex import tokens

# def p_grammar(p):
#     '''
#     abin    : VAZIO
#             | var indent '(' abin ')' '(' abin end_indent ')'
#     var     : NUM
#             | PAL
#     '''

def p_abin_empty(p):
    'abin : VAZIO'
    p[0] = p[1]

def p_indent(p):
    'indent : '
    parser.indent_level += 1

def p_end_indent(p):
    'end_indent : '
    parser.indent_level -= 1

def p_abin_abin(p):
    "abin : var indent '(' abin ')' '(' abin end_indent ')' "
    padding = '\t'
    main_indent_level = padding * parser.indent_level
    p[0] = f"""{{
{padding}{main_indent_level}'root': {p[1]},
{padding}{main_indent_level}'left': {p[4]},
{padding}{main_indent_level}'right': {p[7]}
{padding * parser.indent_level}}}"""

def p_var_NUM(p):
    'var : NUM'
    p[0] = int(p[1])

def p_var_PAL(p):
    'var : PAL'
    p[0] = p[1]

def p_error(p):
    print(f'Syntax error on', p)
    parser.success = False
    pass

out_ = open(sys.argv[1], 'w') if len(sys.argv) > 1 else sys.stdout
in_= open(sys.argv[2], 'r') if len(sys.argv) > 2 else sys.stdin
parser = yacc.yacc()
parser.success = True
parser.indent_level = 0
parsed_output = parser.parse(in_.readline())
if parser.success:
    print(parsed_output, file=out_)
