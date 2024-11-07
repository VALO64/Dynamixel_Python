from libs.motor import Motor

# Crear una instancia del motor con ID 11
#motor_11 = Motor(ID=11)

# Crear una instancia del motor con ID 17
#motor_17 = Motor(ID=17)
motor_13 = Motor(ID=13)
# Mover el motor con ID 11 a una posición específica con cierta velocidad
#motor_11.mov_to(pos=256, vel=200)  # Puedes cambiar pos y vel según necesites

# Mover el motor con ID 17 a una posición diferente con otra velocidad
#motor_17.mov_to(pos=511, vel=150)  # Puedes cambiar pos y vel según necesites
motor_13.mov_to(pos=511, vel=200)  # Puedes cambiar pos y vel según necesites
