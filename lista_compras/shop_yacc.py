from shop_lex import tokens, literals
import ply.yacc as yacc
import sys

'''
statements  : statement
            | statements statement

statement   : ID ':' products

products    : product
            | products product

product     : '-' UINT SEP ID SEP DOUBLE SEP UINT ';'
'''

def p_statements_list(p):
    "statements : statements statement"
    if not p[1]:
        p[1] = []
    if p[2]:
        p[1].append(p[2])
    global result
    p[0] = p[1]


def p_statements(p):
    "statements : statement"
    if not p[0]:
        p[0] = []
    if p[1]:
        p[0].append(p[1])
    global result
    result = p[0]


def p_statement(p):
    "statement   : ID ':' products"
    if p[1] not in parser.categories:
        parser.categories[p[1]] = p[3]
        p[0] = parser.categories
    else:
        print(f"""Category {p[1]} already defined
Proceeding ignoring this category
""")


def p_products(p):
    "products : product"
    if not p[0]:
        p[0] = []
    if p[1]:
        p[0].append(p[1])


def p_products_list(p):
    "products : products product"
    if not p[1]:
        p[1] = []
    if p[2]:
        p[1].append(p[2])
    p[0] = p[1]


def p_product(p):
    "product : '-' UINT SEP ID SEP DOUBLE SEP UINT ';'"
    if p[2] not in parser.products:
        parser.products[p[2]] = p[4]
        p[0] = {
            'id': p[2],
            'name': p[4],
            'price': p[6],
            'quantity': p[8]
        }
    else:
        print(f"""Product {p[4]} could not be attributed to ID {p[2]}
    Cause: this ID already belongs to {parser.products[p[2]]}
Proceeding ignoring this item
""")


def p_error(p):
    if not p:
        pass
    print(f'Syntax error on {p} with value {p.value}')


data = sys.stdin

if len(sys.argv) > 1:
    data = open(sys.argv[1], 'r')

parser = yacc.yacc(debug=True)
parser.categories = {}
parser.products = {}
parser.parse(data.read())
print(result)
