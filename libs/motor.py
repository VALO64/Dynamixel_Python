import serial
import time

class Motor:
    def __init__(self, ID=1):
        self.ID = ID & 0xFF  # Asegura que ID esté en el rango de 0 a 255
        self.mensaje = bytearray(20)  # Mensaje del arreglo 
        self.eco = bytearray(20)      # Eco del arreglo
        self.serial_connection = serial.Serial('/dev/ttyUSB0', baudrate=1000000, timeout=1)  # Conexión en ttyUSB0

    def send_to(self, length):
        self.serial_connection.write(self.mensaje[:length])

    def led_on_off(self, on_off):
        LEN = 0x04
        INST = 0x03
        PARAM1 = 0x19
        PARAM2 = on_off & 0xFF
        CHECKSUM = (0xFF - self.ID - LEN - INST - PARAM1 - PARAM2) & 0xFF

        self.mensaje[0:8] = [0xFF, 0xFF, self.ID, LEN, INST, PARAM1, PARAM2, CHECKSUM]
        self.send_to(8)
        time.sleep(0.00057)
        return self.get_response()

    def mov_to(self, pos, vel):
        # Mueve el motor a una posición y velocidad específicas
        LEN = 0x07
        INST = 0x03
        PARAM1 = 0x1E
        PARAM2 = pos & 0xFF
        PARAM3 = (pos >> 8) & 0xFF
        PARAM4 = vel & 0xFF
        PARAM5 = (vel >> 8) & 0xFF
        CHECKSUM = (0xFF - self.ID - LEN - INST - PARAM1 - PARAM2 - PARAM3 - PARAM4 - PARAM5) & 0xFF

        self.mensaje[0:11] = [0xFF, 0xFF, self.ID, LEN, INST, PARAM1, PARAM2, PARAM3, PARAM4, PARAM5, CHECKSUM]
        self.send_to(11)
        time.sleep(0.00069)
        return self.get_response()

    def get_response(self):
        time.sleep(0.02)
        bytesreciv = self.serial_connection.in_waiting
        response = []
        for _ in range(bytesreciv):
            response.append(self.serial_connection.read(1)[0])
        return response

    def scan_ids(self, id_range=range(1, 255)):
        # Escanea los IDs en el rango dado y retorna una lista de IDs activos encendiendo los LEDs
        active_ids = [] # Arreglo para los ids activos
        for motor_id in id_range:
            self.ID = motor_id
            response = self.led_on_off(1)  # Enciende el LED del motor actual

            if response:  # Si hay respuesta, el ID está activo
                print(f"ID {motor_id} activo, respuesta: {response}")
                active_ids.append(motor_id)
            else:
                print(f"ID {motor_id} no respondió.")
            time.sleep(0.1)  # Pausa para evitar saturar la conexión
        return active_ids
