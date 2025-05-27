'''5 - Crie um programa que use um loop for para imprimir apenas os números ímpares de 1 a 10, pulando os pares com o comando continue.'''

for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(f"Número ímpar: {numero}")