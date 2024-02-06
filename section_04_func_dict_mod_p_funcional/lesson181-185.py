# 181 - 185. Ambientes virtuais em python (venv)
'''

https://pypi.org/

Um ambiente virtual carrega toda a sua instalação
do Python para uma pasta no caminho escolhido.

Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.

Venve é um módulo que vamos utilizar para criar ambientes virtuais.

Podemos dar o nome que desejarmos para o ambiente virtual, mas é comumente chamado:
    - venv
    - env
    - .venv
    - .env

Essa pasta armazena todas as intalações e lib de terceiros.

OBS(1): Não precisa salvar a pasta venv p/ o repositório, pois podemos criar
um arquivo chamado requirements.txt onde inserimos todas infos daquele ambiente virtual
para recriar o venv.

Podemos criar em qualquer lugar o ambiente virtual, mas é aconselhável deixar dentro do programa.

OBS(2): Para Windows é necessário dar get-Executionpolicy no terminal no powershell como adm e se estiver como 'restrict', basta usar o comando 'set-Executionpolicy allsigned'.

Se por acaso você não autorizar quando solicitar no terminal, basta vc utilizar o comando no powershell 'Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser'

'''

# P/ Windows -> Tem que liberar o execution policy para o modo 'unrestrict'

# 1) CRIAR UM AMBIENTE VIRTUAl(digitar no terminal): python -m venv venv

#gcm python ou gcm python -Syntax -> mostra o caminho/path (Windows)
# which python -> mostra o caminho/path (MAC/ Linux)


# 2) ATIVAR O AMBIENTE VIRTUAL(ficará escrito (venv) no terminal):
# (terminal): .\venv\Scripts\activate

# 3) DESATIVAR O AMBIENTE VIRTUAL:
# (terminal): deactivate

# 4) INSTALAR pacotes com o ambiente virtual ativo 'pip' (python package index)
# exp: pip install pymsyql OU python -m pip install pymysql

# 5) DESINSTALAR package: pip uninstall pymysql ou 
# pip uninstall pymysql -y (dessa forma não solicita confirmação de desinstalação)

# LISTAR PACOTES INSTALADOS no ambiente virtual - pip freeze

# LISTA AS VERSÕES DISPONÍVEIS: pip index versions pymysql


# REQUIREMENTS.TXT
'''
O arquivo requirements.txt tem a função de criar um arquivo 
com os requerimentos para rodar o ambiente virtual. 

Dessa forma, evitamos de subir todo ambiente criado em um repositório.

Obs: podemos ter mais de um arquivo requirements.
'''

# COMANDO P/ CRIAR: pip freeze > requirements.txt

#  INSTALAR PACKAGE DESCRITO no requirements.txt: pip install -r .\requirements.txt
