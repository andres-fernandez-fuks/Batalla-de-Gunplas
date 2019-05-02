import random

class Piloto():
    '''Inteligencia artificial para controlar un Gunpla.'''
    
    def __init__(self):
        '''Crea un piloto y no recibe ningun parámetro'''
        self.gunpla = None
        self.nombre = None

    def __repr__(self):
        ''' Devuelve una cadena que representa los stats del piloto'''
        cadena = "\n----Piloto----\n"
        cadena += "    {}\n".format(self.nombre)
        if self.gunpla:
            cadena += "{}".format(repr(self.gunpla))
        return cadena

    def __str__(self):
        '''Devuelve una cadena que representa al piloto'''
        cadena = "{}".format(self.nombre) 
        if self.gunpla:
            cadena += " del {}".format(self.gunpla)
        return cadena

    def set__Gunpla_(self, _Gunpla_):
        '''Asigna un Gunpla a un piloto'''
        self.gunpla = _Gunpla_

    def get__Gunpla_(self):
        '''Devuelve el Gunpla asociado al piloto'''
        return self.gunpla

    def elegir_esqueleto(self,lista_esqueletos):
        '''Dada una lista con esqueletos, devuelve el índice del esqueleto a utilizar'''
        return lista_esqueletos.index(random.choice(lista_esqueletos))

    def elegir_parte(self,partes_disponibles):
        '''Dado un diccionario: {tipo_parte:parte}, devuelve el tipo de parte que quiere 
        elegir. Este metodo se utiliza para ir eligiendo de a una las partes que se van
        a reservar para cada piloto, de entre las cuales va a poder elegir para armar su 
        modelo'''
        claves = list(partes_disponibles.keys())
        tipo_de_parte = random.choice(claves)
        return tipo_de_parte

    def elegir_combinacion(self,partes_reservadas):
        '''Dada una lista con partes previamente reservadas, devuelve una lista con las
        partes a utilizar para construir el Gunpla. Este metodo se utiliza para elegir
        las partes que se van a utilizar en el modelo de entre las que se reservaron
        previamente para cada piloto.'''
        partes_elegidas = []
        tipos_de_partes_ocupadas = set()
        while partes_reservadas and len(partes_elegidas) < self.gunpla.esqueleto.slots:
            parte_elegida = partes_reservadas.pop(random.randint(0,len(partes_reservadas)-1))
            if parte_elegida.tipo_de_parte not in tipos_de_partes_ocupadas or parte_elegida.tipo_de_parte == "Arma":
                partes_elegidas.append(parte_elegida) #equivale a partes_elegidas[len(partes_elegidas):] = [parte_elegida].
                tipos_de_partes_ocupadas.add(parte_elegida.tipo_de_parte)
        return partes_elegidas

    def elegir_oponente(self,oponentes):	
        '''Devuelve el índice del Gunpla al cual se decide atacar de la lista de
        oponentes pasada'''
        return oponentes.index(random.choice(oponentes))

    def elegir_arma(self,oponente):
        '''Devuelve el arma con la cual se decide atacar al oponente. Lanza error si no hay armas o ninguna esta lista'''
        armas_listas = []
        for arma in self.gunpla.armamento:
            arma.calcular_tiempo_recarga()
            if arma.esta_lista(): 
                armas_listas.append(arma)	
        arma_elegida = random.choice(armas_listas)
        arma_elegida.disponible = False	
        return arma_elegida