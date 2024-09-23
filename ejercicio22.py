print("*** Bienvenido al sistema de validación***")

USUARIO = "admin"
PASSWORD = "1234"

usuario_ingresado = input("Por favor ingrese su usuario: ")
password_ingresado = input("Por favor ingrese su contraseña: ")

if (usuario_ingresado == USUARIO) and (password_ingresado == PASSWORD):
    print("Bienvenido al sistema")

elif (usuario_ingresado != USUARIO) and (password_ingresado == PASSWORD):
    print("Su usuario es incorrecto")

elif (usuario_ingresado == USUARIO) and (password_ingresado != PASSWORD):
    print("Su contraseña es incorrecta")

else:
    print("Su usuario y contraseña son incorrectos")