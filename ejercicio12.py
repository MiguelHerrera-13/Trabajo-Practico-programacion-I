print("*** Sistema Generador de ID Unico ***")
print()
nombre = input("Cual es tu nombre?: ") 
apellido = input("Cual es tu apellido?: ")
anio_nacimiento = int(input("Cual es tu año de nacimiento?: "))
nombre_mayus = nombre[:2].upper()
apellido_mayus = apellido[:2].upper()
ultimos_dos_anio = str(anio_nacimiento)[-2:]
import random
valor_aleatorio = random.randint(1000, 9999)

print("Hola", nombre + ",")
print("Tu nuevo número de identificación (ID) generado por el sistema es: ", nombre_mayus + apellido_mayus + ultimos_dos_anio + str(valor_aleatorio))
print("Felicidades!") 