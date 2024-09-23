valor_usuario = int(input("Por favor ingrese un valor entre 0 y 5: "))
VALOR_MIN = 0
VALOR_MAX = 5

if (valor_usuario >= VALOR_MIN) and (valor_usuario <= VALOR_MAX):
    print("Valor dentro de rango: ", True)
else:
    print("Valor dentro de rango: ", False)
