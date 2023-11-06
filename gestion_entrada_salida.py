import sqlite3
from datetime import datetime

class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
       

class Entrada:
    def __init__(self, vehiculo, fecha_hora_entrada):
        self.vehiculo = vehiculo
        self.fecha_hora_entrada = fecha_hora_entrada

class Salida:
    def __init__(self, entrada, fecha_hora_salida):
        self.entrada = entrada
        self.fecha_hora_salida = fecha_hora_salida


class Parqueadero:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                            id INTEGER PRIMARY KEY,
                            placa TEXT,
                            entrada DATETIME,
                            salida DATETIME
                        )''')
        self.conn.commit()

    def registrar_entrada(self, placa):
        cursor = self.conn.cursor()
        entrada = datetime.now()
        cursor.execute('INSERT INTO registros (placa, entrada) VALUES (?, ?)', (placa, entrada))
        self.conn.commit()
        return entrada

    def registrar_salida(self, placa, entrada):
        cursor = self.conn.cursor()
        salida = datetime.now()
        cursor.execute('UPDATE registros SET salida = ? WHERE placa = ? AND entrada = ?', (salida, placa, entrada))
        self.conn.commit()
        return salida

  
# Ejemplo de uso:

parqueadero = Parqueadero()

vehiculo1 = Vehiculo("ABC123", "Toyota", "Camry")
entrada1 = parqueadero.registrar_entrada(vehiculo1)

# Simulamos un tiempo de estadía (por ejemplo, 2 horas)
import time
time.sleep(2 * 3600)

salida1 = parqueadero.registrar_salida(entrada1)

vehiculo2 = Vehiculo("XYZ789", "Honda", "Civic")
entrada2 = parqueadero.registrar_entrada(vehiculo2)

# Simulamos un tiempo de estadía (por ejemplo, 1.5 horas)
time.sleep(1.5 * 3600)

salida2 = parqueadero.registrar_salida(entrada2)



