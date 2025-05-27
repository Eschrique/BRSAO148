'''3 - Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0. O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".'''

inicio = int(input("Digite um número para a contagem regressiva: "))
while inicio >= 0: # o while verifica a condição antes de cada repetição
    print(inicio)
    inicio -= 1 # diminui um valor para cada repetição
print("FIM!")