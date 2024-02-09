# 203. manter e manipular estados dentro da classe

class Camera:
    def __init__(self, name, filmando=False):
        #parameter
        self.name = name
        self.filmando = filmando
    
    # methods
    def filmar(self):
        if self.filmando:
            print(f'{self.name} já está filmando...')
            return
        
        print(f'{self.name} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.name} Não pode fotografar filmando...')
            return
        print(f'{self.name} está fotografando...')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.name} NÃO está filmando...')
            return
        print(f'{self.name} está parando de filmar...')
        self.filmando = False

c1 = Camera('Canon')
c1.filmar()
print('Estado:', c1.filmando) # guardou o estado

# tentar gravar novamente:
c1.filmar()

#tentar fotografar:
c1.fotografar()

# Parar de filmar:
c1.parar_filmar()

# Fotografar:
c1.fotografar()


print()
c2 = Camera('Sony')
c2.filmar()
print('Estado:', c2.filmando)
c2.fotografar()