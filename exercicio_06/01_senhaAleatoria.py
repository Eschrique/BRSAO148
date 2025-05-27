'''1 - Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.'''

import random # Importando o módulo RANDOM
import string # Importando o módulo de caracteres prontos
tamanho = int(input("Informe o tamanho de caracteres para gerar a senha: "))
'''Bloco para definir caracteres que serão usados.
ascii - trazendo letras maiúsculas e minsculas
digits - trazendo números de 0 a 9.
punctuation - Trazendo caracteres especiais.
'''
caracteres_possiveis = string.ascii_letters + string.digits + string.punctuation
'''Bloco de gerar senha
random.choises - escolhe tamanho dos elementos na lista.
'''
senha_lista = random.choices(caracteres_possiveis, k=tamanho)
senha = "".join(senha_lista) # Aqui esta unido os caracteres.
print("Senha gerada: ", senha)