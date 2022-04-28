# Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:

# a. Imprima o resultado da soma de todos os valores da matriz no terminal;

import random
import numpy

matriz_10x10_A = []

for linha in range(1, 11):

    linha_auxiliar_A = []

    for coluna in range(1, 11):
        NumAle = random.randrange(1, 100)
        linha_auxiliar_A.append(NumAle)
    
    matriz_10x10_A.append(linha_auxiliar_A)

matriz_10x10_A = numpy.array(matriz_10x10_A)
print('--- Matriz 10 x 10 A ---')
print(matriz_10x10_A)
print('=' * 100)


for linha in matriz_10x10_A:
    linhas_somadas = []
    soma_das_linhas = 0
    for coluna in linha:
        soma_das_linhas += coluna
        linhas_somadas.append(soma_das_linhas)

soma_da_matriz_10x10 = 0

for soma in linhas_somadas:
    soma_da_matriz_10x10 += soma

print(f'A soma de todos os números da matriz é igual a {soma_da_matriz_10x10}.')
print('=' * 100)

# b. E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

numeros_multiplicados = []

matriz_10x10_B = numpy.array(matriz_10x10_A)
matriz_10x10_B = matriz_10x10_B * 3

print('--- Nova matriz 10 x 10 ---')
print(matriz_10x10_B)