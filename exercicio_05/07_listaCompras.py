'''7 - Crie um programa que permita ao usuário montar uma lista de compras. O usuário poderá adicionar itens até digitar "fim". Ao final, o programa exibirá todos os itens da lista. O programa deve estar estruturado com uma função main() e ser executado com if __name__ == "__main__":.'''

def main():
    lista_compras = []
    print("Bem-vindo à sua Lista de Compras!")
    while True:
        item = input("Digite um item para adicionar (ou 'fim' para encerrar): ")
        if item.lower() == "fim":
            break
        if item.strip() == "":
            print("Item vazio não foi adicionado. Tente novamente.")
            continue
        lista_compras.append(item)
        print(f"'{item}' foi adicionado à sua lista.")
    print("\nSua lista de compras contém:")
    for i, produto in enumerate(lista_compras, start=1):
        print(f"{i}. {produto}")
if __name__ == "__main__":
     main()

