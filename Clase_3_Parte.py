import random

class Parte():
    '''Representa una parte de un Gunpla.'''

    def __init__(self):
        '''Inicializa los atributos de una parte'''
        self.peso = random.randint(0, 500)
        self.armadura = random.randint(0, 100)
        self.escudo = random.randint(0, 100)
        if self.peso > 200:
            self.velocidad = random.randint(-25,25)
        else:
            self.velocidad = random.randint(0,75)
        self.energia = random.randint(-25, 100)
        self.armamento = []
        self.tipo_de_parte = random.choice(["Backpack", "Arm", "Leg" , "Head" , "Body"] )

    def __str__(self):
        '''Devuelve una cadena que representa las estadisticas de la parte'''
        cadena = ("\n----Parte----\n")
        cadena+= ("    Peso: {}\n".format(self.peso))
        cadena+= ("    Armadura: {}\n".format(self.armadura))
        cadena+= ("    Escudo: {}\n".format(self.escudo))
        cadena+= ("    Velocidad: {}\n".format(self.velocidad))
        cadena+= ("    Energia: {}\n".format(self.energia))
        cadena+= ("    Armamento---: {}\n".format(self.armamento))
        cadena+= ("    Tipo de Parte: {}\n".format(self.tipo_de_parte))
        return cadena
    def __repr__(self):
        '''Devuelve una cadena que representa a la parte'''
        if not self.armamento:
            armamento = "No contiene armas"
        else:
            armamento = self.armamento
        return "{}, {}".format(self.tipo_de_parte , armamento)
    def get_peso(self):
        '''Devuelve el peso total de la parte. Una parte pesa lo que pesa la sumatoria
        de sus armas más el peso base de la parte'''
        return self.peso

    def get_armadura(self):	
        '''Devuelve la armadura total de la parte. Una parte tiene tanta armadura como
        la sumatoria de la armadura de sus armas más la armadura base de la parte'''
        return self.armadura

    def get_escudo(self):
        '''Devuelve el escudo total de la parte. Una parte tiene tanto escudo como la 
        sumatoria del escudo de sus armas más el escudo base de la parte'''
        return self.escudo

    def get_velocidad(self):
        '''Devuelve la velocidad total de la parte. Un Gunpla tiene tanta velocidad como 
        la sumatoria de las velocidades de sus partes y esqueleto'''
        return self.velocidad

    def get_energia(self):
        '''Devuelve la energía total de la parte. La parte tiene tanta energía como la 
        sumatoria de la energía de sus armas más la energía base de la parte'''
        return self.energía

    def get_armamento(self):
        '''Devuelve una lista con todas las armas adosadas a la parte'''
        return self.armamento

    def get_tipo_parte(self):	
        '''Devuelve una cadena que representa el tipo de parte. Ej: "Backpack"'''
        return self.tipo_de_parte

    def _definir_armamento(self,armas):
        '''Recibe una lista de armas, adhiere aleatoriamente armas a la parte, contabilizando sus stats'''
        for i in range (len(armas)):
               self.armamento.append(armas[i])
               self.peso += armas[i].peso
               self.armadura += armas[i].armadura
               self.escudo += armas[i].escudo
               if armas[i].tipo_de_parte != "Arma":
                   self.velocidad += armas[i].velocidad
               self.energia += armas[i].energia