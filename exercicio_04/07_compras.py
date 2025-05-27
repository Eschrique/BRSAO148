'''Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. O usuário pode digitar até 10 itens. Se digitar "fim", o programa para imediatamente (break). Se o item for vazio (só apertar Enter), ele é ignorado com continue. Use try/except para garantir que apenas strings sejam inseridas.'''

compras = []

for i in range(10):
    try:
        item = input(f"Digite o nome do {i+1}º produto (ou 'fim' para encerrar): ")

        if item.lower() == 'fim':
            break

        if item.strip() == "":
            print("Item vazio! Tente novamente.")
            continue

        compras.append(item)

    except Exception as e:
        print(f"Erro inesperado: {e}")
        continue

print("Lista de compras:")
for produto in compras:
    print("-", produto)
