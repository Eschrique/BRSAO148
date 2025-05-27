'''6- Calculadora de Média Escolar
Enunciado:
Desenvolva um programa que solicite o nome de um aluno e suas 3 notas. O programa deve calcular a média e informar se o aluno foi aprovado (média >= 7), está em recuperação (5 <= média < 7) ou foi reprovado (média < 5).'''

aluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do(a) {aluno} é: {media:.2f}")
if media >= 7:
    print("Situação: APROVADO!")
elif media >= 5:
    print("Situação: Recuperação!")
else:
    print("Situação: REPROVADO!")
