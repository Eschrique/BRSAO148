'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()
if origem == "C":
    if destino == "F":
        resultado = (valor * 9/5) + 32
    elif destino == "K":
        resultado = valor + 273.15
    else:
        resultado = valor
elif origem == "F":
    if destino == "C":
        resultado = (valor -32) * 5/9
    elif destino == "K":
        resultado = (valor - 32) * 5/9 + 273.15
    else:
        resultado = valor
elif origem == "K":
    if destino == "C":
        resultado = valor - 273.15
    elif destino == "F":
        resultado = (valor - 273.15) * 9/5 + 32
    else:
        resultado = valor
else:
    resultado = None
if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f} {destino}")
else:
    print("Unidade inválida informada.")