'''Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.'''

# Inicializa uma lista para armazenar as notas válidas
notas = []

# Laço que continuará até o professor digitar "fim"
while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    # Verifica se o professor deseja encerrar a entrada de notas
    if entrada.lower() == 'fim':
        break  # Encerra o laço

    try:
        nota = float(entrada)  # Tenta converter a entrada para número decimal

        # Verifica se a nota está dentro do intervalo válido (0 a 10)
        if 0 <= nota <= 10:
            notas.append(nota)  # Adiciona a nota válida à lista
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")  # Aviso para nota fora do intervalo

    except ValueError:
        # Trata o caso em que a entrada não é um número
        print("Entrada inválida! Digite um número ou 'fim' para encerrar.")

# Após o fim do laço, verifica se alguma nota foi registrada
if len(notas) > 0:
    media = sum(notas) / len(notas)  # Calcula a média das notas
    print(f"Média da turma: {media:.2f}")  # Exibe a média com duas casas decimais
else:
    print("Nenhuma nota válida foi inserida.")  # Caso não haja notas válidas
