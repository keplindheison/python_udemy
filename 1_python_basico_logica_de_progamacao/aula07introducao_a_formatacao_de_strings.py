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