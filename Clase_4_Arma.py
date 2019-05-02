import random

class Arma():
    '''Representa un arma.'''

    def __init__(self):
        '''Inicializa los atributos de un arma'''
        self.peso = random.randint(0, 250)
        self.armadura = random.randint(0, 100)
        self.escudo = random.randint(0, 100)
        self.energia = random.randint(25, 75)
        self.tipo_municion = random.choice(["FISICA","LASER","HADRON"])
        self.tipo_de_arma = random.choice(['MELEE','RANGO'])
        self.clase_de_arma = random.choice(["GN Blade","Cannon","Hammer","Gun","Shield","Explosive","Light Sword","Heat Energy scythe","Micro-missiles","Machine gun"])
        if self.tipo_municion == 'FISICA' or self.tipo_municion == 'LASER':
            self.danio = random.randint(200,500)
        else:
            self.danio = random.randint(250,350)
        self.hits = random.randint(1, 5)
        self.precision = random.uniform(1, 100)
        self.tiempo_recarga = random.randint(1, 4)
        self.tiempo_enfriamiento = self.tiempo_recarga
        self.disponible = True
        self.tipo_de_parte = "Arma"

    def __str__(self):
        ''''Devuelve una cadena que representa las estadisticas del arma'''
        cadena = ("\n----Arma----\n")
        cadena+= ("    Peso: {}\n".format(self.peso))
        cadena+= ("    Armadura: {}\n".format(self.armadura))
        cadena+= ("    Escudo: {}\n".format(self.escudo))
        cadena+= ("    Velocidad: {}\n".format(self.velocidad))
        cadena+= ("    Energia: {}\n".format(self.energia))
        cadena+= ("    Tipo de Municion: {}\n".format(self.tipo_municion))
        cadena+= ("    Tipo de arma: {}\n".format(self.tipo_de_arma))
        cadena+= ("    Clase de arma: {}\n".format(self.Clase_de_arma))
        cadena+= ("    Daño: {}\n".format(self.Daño))
        cadena+= ("    Hits: {}\n".format(self.Hits))
        cadena+= ("    Precision: {}\n".format(self.precision))
        cadena+= ("    Tiempo de recarga: {}\n".format(self.tiempo_recarga))
        cadena+= ("    Disponible: {}\n".format(self.Disponible))
        cadena+= ("    Tipo de parte: {}\n".format(self.tipo_de_parte))
        return cadena
    def __repr__(self):
        '''Devuelve una cadena que representa el arma'''
        return "{},{} {} {}".format(self.clase_de_arma, self.tipo_de_arma , self.tipo_municion, self.danio) 
    def get_peso(self):
        '''Devuelve el peso del arma. Es un valor fijo'''
        return self.peso

    def get_armadura(self):
        '''Devuelve la armadura del arma. Es un valor fijo'''
        return self.armadura

    def get_escudo(self):
        '''Devuelve el escudo del arma. Es un valor fijo'''
        return self.escudo

    def get_energia(self):	
        '''Devuelve la energía del arma. Es un valor fijo'''
        return self.energia

    def get_tipo_municion(self):
        '''Devuelve el tipo de munición del arma: "FISICA"|"LASER"|"HADRON"'''
        return self.tipo_municion


    def get_tipo(self):	
        '''Devuelve el tipo del arma: "MELEE"|"RANGO"'''
        return self.tipo_de_arma

    def get_clase(self):	
        '''Devuelve la clase del arma, la cual es un string. Ejemplo "GN Blade"'''
        return self.clase_de_arma

    def get_danio(self):	
        '''Devuelve el daño de un ataque del arma. Es un valor fijo'''
        return self.danio

    def get_hits(self):
        '''Devuelve la cantidad de veces que puede atacar un arma en un turno. 
        Es un valor fijo'''
        return self.hits

    def get_precision(self):
        '''Devuelve la precisión del arma'''
        return self.precision

    def get_tiempo_recarga(self):
        '''Devuelve la cantidad de turnos que tarda un arma en estar lista'''
        return self.tiempo_recarga

    def calcular_tiempo_recarga(self):
        '''Calcula si el arma debe estar disponible y los turnos que deben faltar para que lo esté'''
        if self.tiempo_enfriamiento == 0:
            self.disponible = True
            self.tiempo_enfriamiento = self.tiempo_recarga
        elif self.disponible == False:
            self.tiempo_enfriamiento -= 1

    def esta_lista(self):
        '''Devuelve si el arma es capaz de ser utilizada en este turno o no'''
        return self.disponible

    def get_tipo_parte(self):
        '''Devuelve el tipo de parte de un arma. Siempre es "Arma"'''
        return self.tipo_de_parte

    def es_combinable(self, posible_arma):
        '''Recibe dos armas, las compara para ver si son compatibles, devuelve un booleano como resultado'''
        combinable = False
        if self.get_tipo() == posible_arma.get_tipo():
            if self.get_clase() == posible_arma.get_clase():
                if self.get_tipo_municion() == posible_arma.get_tipo_municion():
                    combinable = True
        return combinable