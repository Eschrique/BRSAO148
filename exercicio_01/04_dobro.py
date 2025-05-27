''' 4 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário. '''

# 'def" Define uma função chamada "dobro" que vai receber um parâmetro chamado "numero"
def dobro(numero):
    # Retorna o valor do número multiplicado por 2
    return numero * 2
# Solicita ao usuário que digite um número
valor = float(input("Digite um número para calcular: "))
# Chama a função "dobro" passando o valor digitado e armazena o resultado
resultado = dobro(valor)
# Exibe o resultado em tela
print("O dobro do número é:", resultado)