'''Crie um programa que solicite ao usuário a idade de várias pessoas. Armazene apenas idades válidas (entre 0 e 120) em uma lista. Use for, try/except, continue para ignorar entradas inválidas, e break para encerrar o programa se o usuário digitar "fim". No final, exiba a lista das idades válidas.'''

idades = []

for i in range(100):  # Limite máximo de 100 tentativas, pode ser ajustado
    entrada = input("Digite a idade (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break  # Encerra o loop se o usuário quiser parar

    try:
        idade = int(entrada)

        if 0 <= idade <= 120:
            idades.append(idade)
        else:
            print("Idade inválida! Deve estar entre 0 e 120.")
            continue  # Volta ao início do laço

    except ValueError:
        print("Valor inválido! Digite apenas números inteiros.")
        continue  # Pula essa tentativa

print(f"Idades válidas registradas: {idades}")
