''' Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
** Instale o modulo requests - pip install requests **
URL da API com base na moeda informada
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL" '''

# Importa os módulos necessários
import requests  # Usado para fazer requisições HTTP
from datetime import datetime  # Usado para converter timestamps em datas legíveis

def consultar_cotacao():
    # Solicita que o usuário informe o código da moeda (ex: USD, EUR, GBP)
    moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").strip().upper()

    # Monta a URL para a API com a moeda informada e BRL como moeda de referência
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        # Faz a requisição GET para a API
        resposta = requests.get(url)

        # Verifica se a resposta foi bem-sucedida (status code 200)
        if resposta.status_code == 200:
            # Converte o conteúdo da resposta para JSON (dicionário Python)
            dados = resposta.json()

            # A chave esperada na resposta é o código das duas moedas juntas, sem hífen (ex: GBPBRL)
            chave = f"{moeda}BRL"

            # Verifica se a chave existe no dicionário de resposta
            if chave in dados:
                # Pega os dados da moeda
                info = dados[chave]

                # Extrai e formata as informações desejadas
                nome = info['name']
                valor_atual = info['bid']
                valor_maximo = info['high']
                valor_minimo = info['low']
                data_hora = datetime.fromtimestamp(int(info['timestamp'])).strftime('%d/%m/%Y %H:%M:%S')

                # Exibe os dados no terminal
                print(f"\nCotação de {nome}")
                print(f"Valor atual  : R$ {valor_atual}")
                print(f"Valor máximo : R$ {valor_maximo}")
                print(f"Valor mínimo : R$ {valor_minimo}")
                print(f"Atualizado em: {data_hora}")
            else:
                # Caso a chave não esteja presente nos dados
                print("Moeda não encontrada na API.")
        else:
            # Caso a API não responda com sucesso
            print("Erro ao consultar a API. Verifique a moeda informada.")
    except Exception as erro:
        # Captura erros inesperados (como problemas de rede)
        print(f"Erro inesperado: {erro}")

# Executa a função
consultar_cotacao()

