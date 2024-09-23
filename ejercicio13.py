print("*** Sistema Autenticación ***")
print()
usuario_ingresado = input("Cual es tu usuario?: ")
contrasena_ingresada = input("Cual es tu contraseña?: ")
USUARIO = "admin"
PASSWORD = "123"

if (usuario_ingresado == USUARIO) and (contrasena_ingresada == PASSWORD):
    print("¿Datos correctos?", True)    
else:
    print("¿Datos correctos?", False)
