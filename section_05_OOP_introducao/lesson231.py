# 231-232. Teoria: polimorfismo, assinatura de métodos e Liskov Substitution Principle
"""
Polimorfismo é o príncipio que permite que classes derivadas de uma mesma SUPERCLASSE
tenham métodos iguais (com a mesma assinatura), mas comportamentos diferentes.

Assinatura do método (livros) = mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)

Assinatura do método (professor) =
    nome do método, 
    qtd.parâmetros que o método possuí,
    tipos de parâmetros,
    retornos do método.

SO"L"ID - Princípio da substituição de liskov:
    - Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse
sem quebrar a aplicação.
    Em resumo, onde vc usar uma superclasse, qualquer subclasse da superclasse deve
    substituir a superclasse.

Dicas extras:
    - Sobrecarga de métodos (Python NÃO SUPORTA)
    - Sobreposição/sobrescrever de métodos (Python suporta)
    - Type Hint: São um recurso que permite especificar o tipo de dados de uma variável em seu código.
"""

from abc import ABC, abstractmethod

class Notificacao(ABC):
    
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    # É p/ retornar bool:
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    
    def enviar(self) -> bool:
        print('Email: enviando:', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return True

# type hint
# notificar() == polimorfismo
def notificar(notificacao: Notificacao):
    
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação Enviada')
    else:
        print('Notificação não enviada')

notificacao_email = NotificacaoEmail ('Testando e-email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS ('Testando e-sms')
notificar(notificacao_sms)