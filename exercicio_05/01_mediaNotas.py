'''Crie uma função que receba uma lista de notas (valores float) e calcule a média. O programa principal deverá solicitar ao usuário o nome de um aluno e suas 3 notas, e então utilizar a função para calcular e exibir a média com duas casas decimais.'''

# Define a função chamada calcular_media que recebe uma lista de notas como argumento
def calcular_media(notas):
    # Calcula a soma das notas e divide pela quantidade de notas para obter a média
    media = sum(notas) / len(notas)
    return media  # Retorna o valor da média

# A partir daqui é o programa principal (fora da função)

# Solicita ao usuário o nome do aluno
aluno = input("Digite o nome do aluno: ")

# Cria uma lista vazia onde serão armazenadas as 3 notas do aluno
notas_aluno = []

# Usa um laço for para pedir 3 notas ao usuário
for i in range(1, 4):  # Vai de 1 até 3
    while True:  # Laço infinito até que uma nota válida seja digitada
        try:
            # Solicita a nota e tenta converter para float
            nota = float(input(f"Digite a {i}ª nota: "))
            # Verifica se a nota está dentro do intervalo válido (0 a 10)
            if 0 <= nota <= 10:
                notas_aluno.append(nota)  # Adiciona a nota à lista
                break  # Sai do while se a nota for válida
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            # Trata o erro se o valor digitado não puder ser convertido para float
            print("Entrada inválida. Digite um número válido.")

# Chama a função calcular_media passando a lista de notas como argumento
media_final = calcular_media(notas_aluno)

# Exibe a média do aluno formatada com duas casas decimais
print(f"A média de {aluno} é: {media_final:.2f}")

# Verifica a situação do aluno com base na média
if media_final >= 7:
    print("Situação: Aprovado")
elif media_final >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
