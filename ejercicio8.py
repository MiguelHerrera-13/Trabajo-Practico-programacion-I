nombre_usuario = "Alfredo Vazquez"
empresa_terciario = "Instituto Educativo Superior Manuel Belgrano"
dominio = ".com.ar"
nombre_usuario_norm = ".".join([palabra.lower() for palabra in nombre_usuario.split()])
separador = empresa_terciario.split()
iniciales_empresa = "".join([palabra[0].lower() for palabra in separador]) 

print("*** Generador de Email ***")
print()
print("Nombre de usuario:", nombre_usuario)
print("Nombre usuario normalizado:", nombre_usuario_norm)
print()
print("Nombre empresa:", empresa_terciario)
print("Extension del dominio:", dominio)
print("Dominio del email normalizado:", "@" + iniciales_empresa + dominio)
print()
print("Email final generado:", nombre_usuario_norm + "@" + iniciales_empresa + dominio)

