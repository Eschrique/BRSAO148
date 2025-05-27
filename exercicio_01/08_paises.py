'''8 - Crie um programa que armazene nomes de países e suas capitais em um dicionário. O usuário digita o nome do país e o programa mostra a capital correspondente.'''

capitais = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Japão": "Tóquio"
}
pais = input("Digite o nome de um pais: ")
if pais in capitais:
    print("A capital de", pais, "é:", capitais[pais])
else:
    print("Pais não encontrado.")