from shop_lex import tokens, literals
import ply.yacc as yacc
import sys

'''
sections    : section
            | sections section

section   : ID ':' products

products    : product
            | products product

product     : '-' UINT SEP ID SEP DOUBLE SEP UINT ';'
'''

def p_sections_list(p):
    "sections : sections section"
    if p[2]:
        p[1].append(p[2])
    p[0] = p[1]


def p_sections(p):
    "sections : section"
    p[0] = [p[1]]


def p_section(p):
    "section   : ID ':' products"
    if p[1] not in parser.categories:
        parser.categories[p[1]] = p[3]
        p[0] = parser.categories
    else:
        parser.success = False
        print(f"""Category {p[1]} already defined
Proceeding ignoring this category
""")


def p_products(p):
    "products : product"
    p[0] = [p[1]]


def p_products_list(p):
    "products : products product"
    if p[2]:
        p[1].append(p[2])
    p[0] = p[1]


def p_product(p):
    "product : '-' UINT SEP ID SEP DOUBLE SEP UINT ';'"
    if p[2] not in parser.products:
        parser.products[p[2]] = p[4]
        parser.products_total += 1
        parser.price_total += float(p[6]) * int(p[8])
        p[0] = {
            'id': p[2],
            'name': p[4],
            'price': p[6],
            'quantity': p[8]
        }
    else:
        parser.success = False
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
parser.success = True
parser.products_total = 0
parser.price_total = 0
result = parser.parse(data.read())

# por enquanto, debug
# fazer totais (estatísticas)
print(result)
if parser.success:
    print("Total de produtos:", parser.products_total)
    print("Preço dos produtos:", parser.price_total)
