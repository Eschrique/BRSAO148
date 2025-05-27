'''Crie uma função que calcule a idade de uma pessoa em dias, com base no ano de nascimento informado pelo usuário.
O programa deve considerar o ano atual como base para o cálculo.
Use try/except para tratar erros de entrada e valide que o ano não pode ser maior que o ano atual.'''

# Importa a biblioteca datetime para obter o ano atual
from datetime import datetime

# Define a função que calcula a idade em dias com base no ano de nascimento
def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade em dias com base no ano de nascimento.
    Parâmetro:
        ano_nascimento (int): Ano de nascimento da pessoa
    Retorno:
        int: idade estimada em dias
    """
    ano_atual = datetime.now().year  # Pega o ano atual usando a data do sistema
    idade_anos = ano_atual - ano_nascimento  # Calcula a idade em anos
    idade_dias = idade_anos * 365  # Estima idade em dias (sem considerar anos bissextos)
    return idade_dias  # Retorna a idade estimada em dias

# Início do programa principal
while True:
    try:
        # Solicita ao usuário o ano de nascimento
        entrada = input("Digite o ano de nascimento (ou 'sair' para encerrar): ")

        # Verifica se o usuário deseja sair do programa
        if entrada.lower() == 'sair':
            print("Programa encerrado.")
            break  # Sai do laço

        # Converte a entrada para inteiro
        ano = int(entrada)

        ano_atual = datetime.now().year  # Obtém novamente o ano atual

        # Verifica se o ano é válido (não pode ser no futuro)
        if ano > ano_atual:
            print("O ano de nascimento não pode ser maior que o ano atual.")
            continue  # Volta ao início do laço

        # Chama a função para calcular a idade em dias
        idade_dias = calcular_idade_em_dias(ano)

        # Exibe o resultado para o usuário
        print(f"Sua idade estimada em dias é: {idade_dias} dias.")

        # Após o cálculo com sucesso, encerra o programa
        break

    except ValueError:
        # Caso a conversão da entrada para inteiro falhe
        print("Entrada inválida. Por favor, digite um ano válido (ex: 1990) ou 'sair'.")
