print("Bienvenido al sistema para comparar dos números")

num1 = int(input("Por favor ingrese el primer número: "))
num2 = int(input("Por favor ingrese el segundo número: "))

if num1 > num2:
    print(num1, "es mayor que", num2)
elif num2 > num1:
    print(num2, "es mayor que", num1)
else:
    print("Los números son iguales")