import unittest
import json
from flask import Flask
from app import app


class CustomTestResult(unittest.TestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f'{test}: ("exito")')

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f'{test}: ("fracaso")')

    def addError(self, test, err):
        super().addError(test, err)
        print(f'{test}: ("error")')


class CustomTextTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult




class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    #Caso de exito para la obtencion de contactos a partir de nuestro numero
    def test_get_contactos(self):
        
        # realizar una solicitud POST a la ruta '/billetera/contactos' con los datos del numero
        response = self.client.get("/billetera/contactos?minumero=21345")
        data = response.data()

        # verificar si la respuesta es exitosa y contiene la clave 'ok' con valor True
        self.assertTrue(data["ok"])

    #Caso de fracaso con el valor del numero no seteado 
    def test_get_contactos(self):
        
        # realizar una solicitud POST a la ruta /billetera/contactos' sin datos adicionales
        response = self.client.get("/billetera/contactos")
        data = response.data()

        # verificar si la respuesta es exitosa y contiene la clave 'ok' con valor True
        self.assertTrue(data["ok"])


if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner())