# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET
# e em que posições se encontram.

import random


VET = []

for x in range(1, 51):
    NumAle = random.randrange(1, 50)
    VET.append(NumAle)

print(VET)
print('-' * 100)

for i in range(0, len(VET)):
    
    print(f'VALOR TESTADO: {VET[i]} | ÍNDICE TESTADO: {i}')
    
    for j in range(0, len(VET)):
        
        if VET[i] == VET[j] and i != j:
            print(f'Índice: {j} | Valor: {VET[j]} \n')