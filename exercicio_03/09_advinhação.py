import random  # Importa o módulo random para gerar números aleatórios

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Inicializa a variável de tentativas
tentativas = 0

# Mensagem inicial
print("Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

# Loop que continuará até o usuário acertar o número
while True:
    # Solicita ao usuário um palpite e converte para inteiro
    palpite = int(input("Digite seu palpite: "))
    
    # Incrementa a quantidade de tentativas
    tentativas += 1

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        break  # Sai do loop se acertar
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")

