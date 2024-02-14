# 211. method vs @classmethod vs @staticmethod
'''
method - self, método de instância
Obs: toda vez que precisarmos utilizar alguma coisa de self,
SEMPRE será um método de instância
DICA: Precisa de um self dentro do method? "Sim", então é um método de instância.

@classmethod - cls, método de classe
    - precisou usar a classe: Usar o @classmethod

@staticmethod - método estático que não possuí 'self' e 'cls'
'''

class Connection:

    #method init: inicia os valores da instância
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)

# method
c1 = Connection()
c1.set_user('Luiz')
c1.set_password('123')
print(c1.user, c1.password)

#@classmethod
c2 = Connection.create_user_auth('Marcos', '234')
print(c2.user, c2.password)

#@staticmethod
print(Connection.log('Mensagem de log!'))
