from libs.motor import Motor
# Pre set pata comienza con ID 7
motor_7 = Motor(ID=7)
motor_9 = Motor(ID=9)
motor_11 = Motor(ID=11)

motor_7.mov_to(pos=511, vel=100)  # Puedes cambiar pos y vel según necesites
motor_9.mov_to(pos=511, vel=100)  # Puedes cambiar pos y vel según necesites
motor_11.mov_to(pos=511, vel=100)  # Puedes cambiar pos y vel según necesites
