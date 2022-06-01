"""
Iniciar com letra, pode conter números, separar _, letras minúsculas

"""
nome = 'Luiz'

# print(nome, type(nome))

nome = 'Keplin Dheison'
idade = 23  #  int
altura = 1.78  #  flot
e_maior = idade > 18  #  bool
data_1 = True  #  bool
data_atual = 2022  #  int
peso = 60  #  int
imc = peso / (altura * altura)

print('Nome:' , nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior: ', e_maior)

print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
