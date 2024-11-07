from libs.motor import Motor
import os

motor = Motor()

# Escanear IDs en el rango de 1 a 254
active_ids = motor.scan_ids(range(1, 255))

# Imprimir los IDs activos encontrados
print("IDs activos encontrados:", active_ids)

# Solicitar el nombre del archivo al usuario
file_name = input("Ingresa el nombre del archivo (sin extensión): ") + ".py"

# Crear el archivo con el nombre proporcionado, con instancias de Motor y comandos mov_to para cada ID activo
with open(file_name, "w") as file:
    file.write("from libs.motor import Motor\n\n")

    # Primero escribimos todas las instancias de motores con los IDs activos
    for id_activo in active_ids:
        file.write(f"motor_{id_activo} = Motor(ID={id_activo})\n")
    
    file.write("\n")  # Separador entre instancias y comandos mov_to

    # Luego escribimos todos los comandos mov_to para cada motor
    for id_activo in active_ids:
        file.write(f"motor_{id_activo}.mov_to(pos=511, vel=100)  # Puedes cambiar pos y vel según necesites\n")

print(f"Archivo '{file_name}' creado con los IDs activos y comandos mov_to.")
