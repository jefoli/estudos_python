# Exercícios:

'''
1) Aumentar os preços dos produtos em 10% e gerar novos_produtos em deep copy (cópia profunta)
'''

'''
2) Ordene os produtos por nome decrescente (do maior para menor) e gere
produtos ordenados por nome por deep copy (cópia profunda)
'''

'''
3) Ordene os produtos por preço crescente (do menor para maior) e
gere produtos ordenados por preço por deep copy (cópia profunda)
'''
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_precos(args):
    arg_recebido = args
    nova_lista = copy.deepcopy(arg_recebido)
    for _, valor in enumerate(nova_lista): 
        valor['preco'] += round((valor['preco']* 0.10))
    return nova_lista
            
aumentar_valor = aumentar_precos(produtos)
print('Nova lista 1:', aumentar_valor)


def ordenar_nomes_decrescente(args):
    ordenador = args
    nova_lista_2 = copy.deepcopy(ordenador)
    nova_lista_2.sort(key=lambda x : x['nome'], reverse=True)
    return nova_lista_2

ord_nomes_decrescente = ordenar_nomes_decrescente(aumentar_valor)
print('Nova lista 2:', ord_nomes_decrescente)


def ordenar_valores_crescente(args):
    ordenador_valores = args
    nova_lista_3 = copy.deepcopy(ordenador_valores)
    nova_lista_3.sort(key=lambda x : x['preco'])
    return nova_lista_3

ord_valores_crescentes = ordenar_valores_crescente(aumentar_valor)
print('Nova lista 3:', ord_valores_crescentes)


print('Produtos originais:', produtos)


# Proposta de resolução

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
]
print(*novos_produtos)

# 2)
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda p: p['nome'], reverse=True)
print(*produtos_ordenados_por_nome)


produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda p: p['preco'])
print(*produtos_ordenados_por_preco)