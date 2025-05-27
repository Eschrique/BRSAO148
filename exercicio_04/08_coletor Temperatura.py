'''Crie um programa para registrar as temperaturas de vários dias. O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. Valores inválidos devem ser ignorados. Ao final, exiba a média das temperaturas registradas.'''

temperaturas = []

for dia in range(7):
    entrada = input(f"Digite a temperatura do dia {dia+1} (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break  # Encerra se o usuário digitar 'fim'

    try:
        temp = float(entrada)  # Tenta converter para float
        temperaturas.append(temp)
    except ValueError:
        print("Entrada inválida. Digite um número válido (ex: 25.5).")
        continue  # Ignora valores inválidos

# Exibe os resultados
if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"Média das temperaturas: {media:.2f} °C")
else:
    print("Nenhuma temperatura válida foi registrada.")
