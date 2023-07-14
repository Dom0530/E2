import operacion as o
import datetime
class Cuenta:

    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.operaciones = []
        
    def historial(self):
        return self.operaciones
    
    def pagar(self, destino, valor):

        if self.saldo <= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.operaciones.append('Pago realizado de ' + valor +' a '+ destino.nombre)
            destino.operaciones.append('Pago recibido de ' + valor +' de '+ self.nombre)
            return True, datetime.datetime.now()
        else:
            return False, datetime.datetime.now()