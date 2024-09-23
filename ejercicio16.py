monto = int(input("Bienvenido al sistema de la tienda. Por favor ingrese el monto de la compra: "))
miembro_tienda = int(input("Es usted miembro de la tienda? (1 = si, 0 = no): ")) 

if monto >= 1000 and miembro_tienda == 1:
    print("Descuento del 10%")
elif miembro_tienda == 1: 
    print("Descuento del 5%")
else:
    print("Descuento del 0%")
