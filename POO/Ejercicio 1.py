# escriba una clase que represente un vehículo con métodos y atributos. Dentro atributos
# cree uno llamado “placa” y en los métodos cree uno que permita determinar de acuerdo
# con el día (datetime), si el vehículo tiene restricción por pico y placa o no, en la ciudad de Bogotá. 
#los vehiculos circularan: Dias pares (6-7-8-9-0); Dias impares (1-2-3-4-5)

from datetime import datetime

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def pico_y_placa(self):
        ult_num = self.placa[-1]
        dia_hoy = datetime.now().day

        if dia_hoy % 2 == 0:
            if ult_num in ["1", "2", "3", "4", "5"]:
                print(f"El vehículo con placa {self.placa} tiene pico y placa el día de hoy.")
            else:
                print(f"El vehículo con placa {self.placa} NO tiene pico y placa el día de hoy.")
        else:
            if ult_num in ["6", "7", "8", "9", "0"]:
                print(f"El vehículo con placa {self.placa} tiene pico y placa el día de hoy.")
            else:
                print(f"El vehículo con placa {self.placa} NO tiene pico y placa el día de hoy.")

Placa_entrada = input("Ingrese la placa de su vehículo: ")
vehiculo_usuario = Vehiculo(Placa_entrada)

print(f"La placa ingresada es: {vehiculo_usuario.placa}")
vehiculo_usuario.pico_y_placa()