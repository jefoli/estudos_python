# 66-68. Exercício guiado - Calculadora - Parte 1
'''
Requisitos: 
1) Pedir o primeiro número ao usuário
2) Pedir o segundo número ao usuário
3) Pedir um operador de + - // *
4) fazer a operação e retornar o valor
'''
while True:
    result = 0
    exit_option = input('Deseja sair? Digite [s]: ').lower().startswith("s")
    print(20 * '-')

    if exit_option is True:
        break

    first_number = input("Insira o primeiro valor: ")
    second_number = input("Insira o segundo valor: ")

    first_number_check = first_number.isdigit()
    second_number_check = second_number.isdigit()

    if first_number_check and second_number_check is True:
        
        first_number = int(first_number)
        second_number = int(second_number)

        operator = input("Insira o operador: ")
        if operator == "+":
            result += (first_number+second_number)
        elif operator == "-":
            result += (first_number-second_number)
        elif operator == "/":
            result += (first_number/second_number)
        elif operator == "*":
            result += (first_number*second_number)
        else:
            print("Operador desconhecido")
        print(result)

    else:
        print("Digite somente números")
    
