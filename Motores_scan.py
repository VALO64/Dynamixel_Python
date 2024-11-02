from libs.motor import Motor
motor = Motor()

# Escanear IDs en el rango de 1 a 254
active_ids = motor.scan_ids(range(1, 255))

print("IDs activos encontrados:", active_ids)
