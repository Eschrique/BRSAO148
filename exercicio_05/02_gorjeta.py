'''Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
A função deve receber dois parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (por exemplo, 10 para 10%)'''

# Define a função chamada calcular_gorjeta com dois parâmetros: valor_conta e porcentagem_gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta com base no valor da conta e na porcentagem desejada.
    """
    # Calcula o valor da gorjeta: total da conta multiplicado pela porcentagem (dividido por 100)
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta  # Retorna o valor calculado da gorjeta

# A partir daqui começa o programa principal (fora da função)

while True:  # Inicia um laço que só termina quando os valores forem válidos
    try:
        # Solicita o valor total da conta e converte para float
        valor = float(input("Digite o valor total da conta (em reais): R$ "))

        # Solicita a porcentagem da gorjeta e converte para float
        porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

        # Verifica se os valores são positivos
        if valor < 0 or porcentagem < 0:
            print("Os valores devem ser positivos. Tente novamente.")
            continue  # Retorna ao início do laço se os valores forem negativos

        # Chama a função calcular_gorjeta passando os valores digitados
        valor_gorjeta = calcular_gorjeta(valor, porcentagem)

        # Exibe o valor da gorjeta formatado com duas casas decimais
        print(f"A gorjeta a ser deixada é: R$ {valor_gorjeta:.2f}")

        # Encerra o programa após o cálculo com sucesso
        break

    except ValueError:
        # Captura erro caso o usuário digite algo que não pode ser convertido em float
        print("Entrada inválida. Digite números válidos para a conta e a porcentagem.")
