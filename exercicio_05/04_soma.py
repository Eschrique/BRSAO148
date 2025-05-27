'''Crie uma função que recebe dois números e retorna a soma. O programa deve pedir os números ao usuário, chamar a função e exibir o resultado.'''

# Função que soma dois números
def somar(a, b):
    """
    Recebe dois números e retorna a soma deles.
    """
    return a + b

# Bloco principal
if __name__ == "__main__":
    try:
        # Solicita os números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Chama a função e exibe o resultado
        resultado = somar(num1, num2)
        print(f"A soma é: {resultado}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
