tarifa_nacional = 10
tarifa_internacional = 20
print("Bienvenido al sistema para calcular su costo de envío")
print()
destino_usuario = int(input("Por favor ingrese el destino de su paquete (Nacional = 1 o Internacional = 2): "))
peso_paquete_usuario = float(input("Por favor ingrese el peso del paquete: "))

if destino_usuario == 1:
    print(f"El costo del envío es de ${tarifa_nacional * peso_paquete_usuario}")

elif destino_usuario == 2:
    print(f"El costo del envío es de ${tarifa_internacional * peso_paquete_usuario}")