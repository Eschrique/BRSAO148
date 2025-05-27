'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.'''
# Solicita que o usuário digite o primeiro número
numero1 = float(input("Digite o primeiro número: "))
# Solicita que o usuário digite o segundo número
numero2 = float(input("Digite o segundo número: "))
# Solicita que o usuário digite a operação
operacao = input("Digite a operação (+, -, * ou /): ")
# Verifica a operação que o usuário digitou
if operacao == "+":
    # Soma os 2 números
    resultado = numero1 + numero2
    print("O resultado da soma é: ", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("O resultado da subtração é: ", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é: ", resultado)

elif operacao == "/":
    # Verifica se o segundo número é diferente de zero
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado da divisão é: ", resultado)
    else:
        print("Erro: divisão por ZERO não é permitida")
else:
    print("Operação inválida!")