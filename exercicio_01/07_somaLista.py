'''7 - Crie um programa que contenha uma lista com números e calcule a soma total desses números usando um laço for.'''

# Definição de números em uma lista [] - lista
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
soma = 0
for numero in numeros:
    soma += numero
print("A soma dos números é: ", soma)