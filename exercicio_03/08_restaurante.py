# Solicita ao usuário a nota de avaliação (de 0 a 5)
nota = float(input("Avalie o restaurante (0 a 5 estrelas): "))
# Verifica a nota inserida pelo usuário e exibe a classificação correspondente
# Se a nota for igual a 5
if nota == 5:
    print("★★★★★ - Excelente! Comida maravilhosa e ótimo atendimento!")    
# Se a nota for maior ou igual a 4, mas menor que 5
elif nota >= 4:
    print("★★★★☆ - Muito bom! Voltaria com certeza.")    
# Se a nota for maior ou igual a 3, mas menor que 4
elif nota >= 3:
    print("★★★☆☆ - Razoável, mas tem espaço para melhorar.")    
# Se a nota for maior ou igual a 2, mas menor que 3
elif nota >= 2:
    print("★★☆☆☆ - Precisa melhorar em vários pontos.")    
# Se a nota for maior ou igual a 1, mas menor que 2
elif nota >= 1:
    print("★☆☆☆☆ - Experiência ruim, não recomendo.")    
# Se a nota for maior ou igual a 0, mas menor que 1
elif nota >= 0:
    print("☆☆☆☆☆ - Péssimo! Comida e serviço deixaram a desejar.")    
# Caso a nota esteja fora do intervalo de 0 a 5
else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 5.")
