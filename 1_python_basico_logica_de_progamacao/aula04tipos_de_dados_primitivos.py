"""
Tipos de dados 
    str - string - textos 'Assim' ou "Assim"
    int - inteiro - 123456, 0, -20, -50, -60, -15000, 1500
    float - real/ponto flutuante - 1.5, 0.5,  -2.8, 10.10, -50.93, 0.0
    bool - booleano/lógico - True/False

"""
# Função type() retorna o tipo do valor dentro dela
print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))


# Converter um tipo em outro tipo
print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), type(int(10)))

# Nome: str
print('Keplin Dheison Sousa', type('Keplin Dheison Sousa'))

# Idade: int
print(23, type(23))

# Altura: float
print(1.75, type(1.75))

# É maior de idade xx > xx
print(23 > 18, type(23 > 18))

