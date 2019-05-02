import random

class Esqueleto():
    '''Representa el esqueleto interno del Gunpla.'''

    def __init__(self):
        '''Inicializa los atributos de un Esqueleto'''
        self.velocidad = random.randint(-25, 50)
        self.energia = random.randint(1000,2000)
        self.movilidad = random.randint(1000,1500)
        self.slots = random.randint(3, 5)

    def __str__(self):
        '''Devuelve una cadena que representa las estadisticas del esqueleto'''
        cadena = ("\n----Esqueleto----\n")
        cadena+= ("    Velocidad: {}\n".format(self.velocidad))
        cadena+= ("    Energia: {}\n".format(self.energia))
        cadena+= ("    Movilidad: {}\n".format(self.movilidad))
        cadena+= ("    Slots: {}\n".format(self.Slots))
        return cadena

    def get_velocidad(self):
        '''Devuelve la velocidad del esqueleto. Es un valor fijo'''
        return self.velocidad

    def get_energia(self):
        '''Devuelve la energía del esqueleto. Es un valor fijo'''
        return self.energia

    def get_movilidad(self):
        '''Devuelve la movilidad del esqueleto. Es un valor fijo'''
        return self.movilidad

    def get_cantidad_slots(self):
        '''Devuelve la cantidad de slots (ranuras) para armas que tiene el esqueleto. 
        Es un valor fijo'''
        return self.slots