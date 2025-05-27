'''4 - Crie um programa que continue pedindo uma senha ao usuário até que ele digite a senha correta. Quando a senha correta for digitada, o programa mostra uma mensagem de sucesso e interrompe o loop com break.'''

senha_correta = "123456"
while True:
    senha = input("Digita a senha: ")
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")