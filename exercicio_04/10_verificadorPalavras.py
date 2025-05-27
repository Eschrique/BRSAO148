'''Peça ao usuário para digitar palavras. Armazene apenas as palavras com mais de 5 letras em uma lista. Se a palavra for "parar", o programa encerra (break). Se a palavra for numérica (como "123"), ignore com continue. Use try/except para garantir que só palavras (strings) sejam processadas. No final, exiba a lista das palavras longas inseridas.'''

palavras_longas = []

for _ in range(100):  # Limite de 100 palavras (ajustável)
    entrada = input("Digite uma palavra (ou 'parar' para encerrar): ")

    if entrada.lower() == 'parar':
        break  # Encerra o programa

    try:
        if entrada.isnumeric():
            print("Não é permitido inserir apenas números.")
            continue  # Ignora entradas numéricas

        if len(entrada) > 5:
            palavras_longas.append(entrada)
        else:
            print("Palavra muito curta. Deve ter mais de 5 letras.")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        continue  # Ignora outros erros

print("Palavras com mais de 5 letras digitadas:")
for palavra in palavras_longas:
    print("-", palavra)
