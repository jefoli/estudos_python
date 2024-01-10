# 62. while + continue - pulando alguma repetição

counter = 0
while counter <= 100:
    counter += 1

    if counter == 11:
        continue

    if counter >= 20 and counter <= 29:
        print(f'não vou mostrar o {counter}')
        continue
    
    print(f'Counter = {counter}')

    if counter == 40:
        break

