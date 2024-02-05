# 177. filter é um filtro funcional
'''
Filter se baseia no iterável original, porém pode retornar menos elementos.
- 1 param: recebe uma func
- 2 param: recebe um iterável

Article: https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
'''

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

products = [
    {'nome':'produto 5', 'preco': 10.00},
    {'nome':'produto 1', 'preco': 22.32},
    {'nome':'produto 3', 'preco': 10.11},
    {'nome':'produto 2', 'preco': 105.87},
    {'nome':'produto 4', 'preco': 69.90},
]

# filter com list comprehension
filter_new_products = [
    p for p in products if p['preco'] > 10
]
print(filter_new_products)
print()

# func filter:
new_products_2 = filter(lambda p: p['preco'] >= 100, products)
print('func filter:', list(new_products_2))
print()

#filter com lambda:
def filter_price(product):
    return product['preco'] > 100

new_products_3 = filter(filter_price, products)
print(list(new_products_3))
print()
