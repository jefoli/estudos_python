# 58. Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string
# https://docs.python.org/3/library/stdtypes.html
# Tipos imutáveis em python: str, int, float, bool

string = 'luiz Otávio'
# É necessário criar nova var p/ manipular os valores da var principal.
outra_variavel = f'{string[:3]}ABC{string[4:]}' 
print(outra_variavel)

# str.capitalize() - Return a copy of the string with its first character capitalized and the rest lowercased.
print(string.capitalize())

#str.lower()
print(string.lower())

#str.upper()
print(string.upper())

#str.zfill() - Pad a numeric string with zeros on the left, to fill a field of the given width.
print(string.zfill(50))