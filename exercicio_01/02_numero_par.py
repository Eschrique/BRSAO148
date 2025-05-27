''' 2 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar. '''

# Solicita ao ususário que digite um número
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2 (resto é igual a zero)
if numero % 2 == 0:
    # Se o resto da divisão for zero será um número par
    print("O número é par.")
else:
    # Caso contrário será ímpar
    print("O número é impar.")

'''
numero = int(input) - solicita e converte a entrada para um número inteiro
if numero % 2 == 0: - verificar se o número é divisível por 2, caso for o resto será 0, sendo 0 será número par.
else (senão), número ímpar.
print() - mostra o resultado
'''