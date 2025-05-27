'''Peça ao usuário que digite 10 números inteiros. Armazene apenas os números pares válidos em uma lista. Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.'''

pares = []

for i in range(10):
    entrada = input(f"Digite o {i+1}º número inteiro: ")

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            pares.append(numero)
        else:
            print("Número ímpar! Ignorado.")
            continue  # Pula números ímpares

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue  # Pula entrada inválida

print(f"Números pares válidos: {pares}")
