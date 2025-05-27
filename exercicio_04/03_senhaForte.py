'''Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''

import re  # Importa o módulo de expressões regulares (usado para verificar se há números)

# Laço que continuará até que o usuário digite uma senha forte ou "sair"
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    # Verifica se o usuário quer encerrar
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break  # Encerra o laço

    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("Senha fraca: deve conter pelo menos 8 caracteres.")
        continue  # Volta ao início do laço

    # Verifica se a senha contém pelo menos um número
    if not re.search(r"\d", senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue  # Volta ao início do laço

    # Se passou nas duas verificações acima, a senha é considerada forte
    print("Senha forte cadastrada com sucesso!")
    break  # Encerra o laço
