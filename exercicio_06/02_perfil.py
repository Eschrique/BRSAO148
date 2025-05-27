'''2 - Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
** Instale o modulo requests - pip install requests **
URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"'''

# Importamos o módulo requests para fazer chamadas HTTP
import requests

# Bloco principal do programa
def gerar_usuario_aleatorio():
    """
    Essa função se conecta à API 'https://randomuser.me/api/',
    obtém os dados de um usuário aleatório e imprime nome, email e país.
    """
    
    # URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"
    
    # Fazemos uma requisição GET para obter os dados
    resposta = requests.get(url)
    
    # Verificamos se a resposta foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        # Convertendo o conteúdo da resposta para um dicionário Python
        dados = resposta.json()
        
        # Acessando o primeiro (e único) resultado retornado
        usuario = dados['results'][0]

        # Extraindo os dados desejados:
        # - Nome completo (título, primeiro nome e último nome)
        nome_completo = f"{usuario['name']['title']} {usuario['name']['first']} {usuario['name']['last']}"
        # - Email
        email = usuario['email']
        # - País
        pais = usuario['location']['country']
        
        # Exibindo os dados do usuário
        print("=== Perfil de Usuário Gerado ===")
        print("Nome :", nome_completo)
        print("Email:", email)
        print("País :", pais)

    else:
        # Se a requisição falhar, informamos o erro
        print(f"Erro ao acessar a API. Código de status: {resposta.status_code}")

# Chamamos a função principal
gerar_usuario_aleatorio()

