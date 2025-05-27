'''Solicite ao usuário números inteiros até que ele digite "0". Armazene os positivos e negativos separadamente em duas listas. Ignore valores não inteiros com try/except. No final, mostre quantos positivos e negativos foram inseridos.'''

positivos = []
negativos = []

while True:
    entrada = input("Digite um número inteiro (ou 0 para encerrar): ")

    try:
        numero = int(entrada)

        if numero == 0:
            break  # Encerra o loop

        if numero > 0:
            positivos.append(numero)
        else:
            negativos.append(numero)

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        continue  # Pula entrada inválida

# Exibe os resultados
print(f"Total de positivos: {len(positivos)} -> {positivos}")
print(f"Total de negativos: {len(negativos)} -> {negativos}")
