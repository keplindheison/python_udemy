nome = 'Keplin Dheison'
idade = 23  #  int
altura = 1.78  #  flot
e_maior = idade > 18  #  bool
data_1 = True  #  bool
data_atual = 2022  #  int
peso = 60  #  int
imc = peso / (altura * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

"""
* Criar variáveis para nome (str), idade (int),
* Altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""


nome = 'keplin dheison sousa'
idade = 24
altura = 1.78
peso = 60.0
ano = 2022
data_nasc = ano - idade
imc = peso / (altura * altura)

print(f'Nome {nome} tem {idade} anos, e pesa {peso} kilos, nascido no ano de {data_nasc}')
print(f'Seu IMC é {imc:.2f}, ano atual {ano}')



