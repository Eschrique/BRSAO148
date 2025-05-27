'''1 - Crie um programa que solicite ao usuário uma nota (de 0 a 10) e exiba uma mensagem dizendo se o aluno foi reprovado, em recuperação ou aprovado.
Use as estruturas de decisão if, elif e else.'''

nota = int(input("Digite a nota do aluno (0 a 10): "))
if nota >= 7:
    print("Aluno aprovado.")
elif nota >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno foi reprovado.")
    