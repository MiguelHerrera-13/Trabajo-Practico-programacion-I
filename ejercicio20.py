print("Sistema para convertir una clasificación numerica")
print()

numero = int(input("Por favor ingrese un número: "))

if numero >= 9 and numero <= 10:
    print("Su número es: A")

elif numero >= 8 and numero <= 9:
        print("Su número es: B")

elif numero >= 7 and numero <= 8:
        print("Su número es: C")

elif numero >= 6 and numero <= 7:
        print("Su número es: D")

elif numero >= 0 and numero <= 6:
        print("Su número es: F")
else:
    print("Valor desconocido")