'''7 - Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos. Use o for para iterar, if para a verificação e continue para pular os que não são primos.'''

# Lista de números a serem analisados
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19]
for numero in numeros:
    if numero < 2:
        continue      
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False  # Se encontrar um divisor, não é primo
            break  # Não precisa continuar testando
    if eh_primo:
        print(f"{numero} é primo.")
    else:
        continue



  
