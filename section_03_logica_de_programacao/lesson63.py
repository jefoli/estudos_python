# 63. while + while (laços internos)

qtd_lines = 5
qtd_columns = 5
line = 1 

while line <= qtd_columns:
    column = 1
    while  column <= qtd_columns:
        print(f'{line=} {column=}')
        column += 1
    line += 1

print('finish')