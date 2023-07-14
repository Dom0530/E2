import datetime

class Operacion:

    def __init__(self, numero_destino, valor, tipo):
        self.numero_destino = numero_destino
        self.fecha = datetime.datetime.now()
        self.valor = valor
        self.tipo = tipo
