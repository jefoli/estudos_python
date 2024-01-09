'''
# 50-51. Variáveis, constantes e complexidade de código (boas práticas)

a) Em python não temos constantes (item de dados nomeado com um valor predefinido) igual outras linguagens de programação.

Por convenção, variiáveis que não terão seu valor alterado são colocadas em MAIÚSCULO.

CONSTANTE = "Variaveis" que não vão mudar

b) Quanto mais condições no mesmo if, mais complexo será o código (ruim | evitar)

'''
# Exemplo de constantes e variaveis:

VELOCIDADE_MAX_RADAR_1 = 60 #CONST
LOCAL_RADAR = 100 #CONST

velocidade = int(input('Velocidade do veículo: '))
local_carro = 101

# Formas alternativas:

#1
if velocidade > VELOCIDADE_MAX_RADAR_1 and local_carro >= LOCAL_RADAR:
    print('Você passou da velocidade permitida! Carro autuado!')
else:
    print('Velocidade OK.')

#2
aplicar_multa = velocidade > VELOCIDADE_MAX_RADAR_1 and local_carro >= LOCAL_RADAR

if aplicar_multa:
    print('Você passou da velocidade permitida! Carro autuado!')
else:
    print('Velocidade OK.')

#3
velocidade_acima_limite = velocidade > VELOCIDADE_MAX_RADAR_1

local_veículo = local_carro >= LOCAL_RADAR

if velocidade_acima_limite and local_veículo:
    print('Você passou da velocidade permitida! Carro autuado!')
else:
    print('Velocidade OK.')