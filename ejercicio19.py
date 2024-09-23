invierno = [1, 2, 12]
primavera = [3, 4, 5]
verano = [6, 7, 8]
otonio = [9, 10, 11]

print("Sistema de Estaciones del año")
print() 

mes = int(input("Por favor ingrese el numero del mes (1-12): "))

if mes in invierno:
    print("Invierno")
elif mes in primavera:
    print("Primavera")
elif mes in verano:
    print("Verano")
elif mes in otonio:
    print("Otoño")
else:
    print("Estacion desconocida")