'''1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:'''

while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            if numero2 == 0:
                print("Erro: divisão por ZERO não permitido.")
                continue
            resultado = numero1 / numero2
        else:
            print("Erro: operação inválida: Use ( +, -, * , /).")
            continue
        print(f"Resultado: {resultado:.2f}")
        break
    except ValueError:
        print("Erro: digite apenas números.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
