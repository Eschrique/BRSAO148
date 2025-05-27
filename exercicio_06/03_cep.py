'''Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
** Instale o modulo requests - pip install requests **
URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"'''

# Importamos o módulo requests para realizar a consulta HTTP à API do ViaCEP
import requests

# Função principal que consulta o endereço com base no CEP
def consultar_cep():
    """
    Essa função solicita um CEP ao usuário, consulta a API ViaCEP
    e exibe o logradouro, bairro, cidade e estado.
    """

    # Solicitamos o CEP ao usuário
    cep = input("Informe o CEP (somente números): ").strip()

    # Verificação simples: o CEP deve ter exatamente 8 dígitos numéricos
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Deve conter exatamente 8 números.")
        return

    # Montamos a URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Enviamos uma requisição GET para a API
    resposta = requests.get(url)

    # Verificamos se a resposta foi bem-sucedida (HTTP status 200)
    if resposta.status_code == 200:
        # Convertendo o conteúdo da resposta para um dicionário
        dados = resposta.json()

        # Verificamos se o CEP existe. A API retorna {"erro": true} se não existir
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            # Extraímos as informações desejadas
            logradouro = dados.get("logradouro", "N/A")
            bairro     = dados.get("bairro", "N/A")
            cidade     = dados.get("localidade", "N/A")
            estado     = dados.get("uf", "N/A")

            # Exibimos as informações do endereço
            print("\n=== Endereço Encontrado ===")
            print("Logradouro:", logradouro)
            print("Bairro    :", bairro)
            print("Cidade    :", cidade)
            print("Estado    :", estado)
    else:
        # Caso ocorra um erro na comunicação com a API
        print(f"Erro ao consultar o CEP. Código de status: {resposta.status_code}")

# Executamos a função principal
consultar_cep()
