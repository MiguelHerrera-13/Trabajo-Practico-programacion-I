print("="*55)
print("¡Bienvenido al Sistema de Reserva del Hotel!")
print("="*55)
print("Aquí podrá realizar la reserva de su estancia.")
print()
nombre_cliente = input("Por favor ingrese su nombre: ")
dias_estancia = int(input("Por favor ingrese los días de estancia: "))
cuarto = int(input("Por favor ingrese el tipo de habitación (1 = Con vista al mar o 2 = Sin vista al mar): "))

if cuarto == 1:
    total = float(15000 * dias_estancia)
    print(f"El valor total de la estancia es de: ${total:,.0f} por {dias_estancia} días de estancia.")
    print("Su habitación tiene vista al mar.")
elif cuarto == 2:
    total = float(10000 * dias_estancia)
    print(f"El valor total de la estancia es de: ${total:,.0f} por {dias_estancia} días de estancia.")
    print("Su habitación no tiene vista al mar.")