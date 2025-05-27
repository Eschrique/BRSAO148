'''Crie uma função que receba um número como argumento e retorne o quadrado desse número. Depois, chame essa função passando um número digitado pelo usuário.'''

# Define a função que recebe um número e retorna seu quadrado
def calcular_quadrado(numero):
    # Retorna o número multiplicado por ele mesmo
    return numero * numero

# Solicita ao usuário que digite um número
entrada = float(input("Digite um número: "))

# Chama a função e armazena o resultado
resultado = calcular_quadrado(entrada)

# Exibe o resultado na tela
print("O quadrado de", entrada, "é:", resultado)