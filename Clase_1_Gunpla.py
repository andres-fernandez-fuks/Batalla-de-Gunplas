import random

class Gunpla():
    '''Representa un Gunpla. Un Gunpla esta compuesto de un Esqueleto, un conjunto
    de partes y un conjunto de armas.'''

    def __init__(self, Esqueleto):
        '''Inicializa los atributos de un Gunpla'''
        self.peso = 0
        self.armadura = 0
        self.escudo = 0
        self.velocidad = Esqueleto.velocidad
        self.energia = Esqueleto.energia
        self.energia_restante = self.energia
        self.movilidad = 0
        self.armamento = []
        self.esqueleto = Esqueleto
        self.nombre = random.choice(("RX-178 Gundam Mk-II","GAT-X105 Strike","GAT-X102 Duel", "GAT-X103 Buster", "GAT-X207 Blitz", "GAT-X303 Aegis", "MBF-02 Strike Rouge","ORB-01 Akatsuki","ZGMF-X09A Justice", "ZGMF-X10A Freedom Gundam", "ZGMF-X56S Impulse", "ZGMF-X24S Chaos", "ZGMF-X31S Abyss", "ZGMF-X88S Gaia", "ZGMF-X23S Saviour", "GFAS-X1 Destroy", "ZGMF-X666S Legend", "ZGMF-X42S Destiny", "GSX-401FW Stargazer"))#para ver quien es quien

    def __repr__(self):
        '''Devuelve una cadena que representa las estadisticas del gunpla'''
        cadena = ("----Gumpla----\n")
        cadena+= ("    Modelo: {}\n".format(self.nombre))
        cadena+= ("    Peso: {}\n".format(self.peso))
        cadena+= ("    Armadura: {}\n".format(self.armadura))
        cadena+= ("    Escudo: {}\n".format(self.escudo))
        cadena+= ("    Velocidad: {}\n".format(self.velocidad))
        cadena+= ("    Energia: {}\n".format(self.energia))
        cadena+= ("    Energia restante: {}\n".format(self.energia_restante))
        cadena+= ("    Movilidad: {:.2f}\n".format(self.movilidad))
        cadena+= ("    Armamento:")
        for arma in self.armamento:
            cadena+= "\n                {}".format(repr(arma))
        return cadena
    def __str__(self):
        '''Devuelve una cadena que representa al gunpla'''
        return "Gunpla {}".format(self.nombre)    
    def get_peso(self):	
        '''Devuelve el peso total del Gunpla. Un Gunpla pesa lo que pesa la sumatoria
        de sus partes y armas'''
        
        return self.peso

    def get_armadura(self):	
        '''Devuelve la armadura total del Gunpla. Un Gunpla tiene tanta armadura como la 
        sumatoria de la armadura de sus partes y armas'''
        return self.armadura

    def set_armadura(self,armadura): 
        '''Recibe un valor numerico que determina la armadura del Gunpla'''
        self.armadura = armadura

    def get_escudo(self):	
        '''Devuelve el escudo total del Gunpla. Un Gunpla tiene tanto escudo como la
        sumatoria del escudo de sus partes y armas'''
        return self.escudo

    def set_escudo(self,escudo): 
        '''Recibe un valor numerico que determina el escudo del Gunpla'''
        self.escudo = escudo

    def get_velocidad(self):	
        '''Devuelve la velocidad total del Gunpla. Un Gunpla tiene tanta velocidad como
        la sumatoria de las velocidades de sus partes y esqueleto'''
        return self.velocidad

    def get_energia(self):	
        '''Devuelve la energía total del Gunpla. Un Gunpla tiene tanta energía como la
        sumatoria de la energía de sus partes, armas y esqueleto'''
        return self.energia

    def get_energia_restante(self):	
        '''Devuelve la energía que le resta al Gunpla'''
        return self.energia_restante

    def get_movilidad(self):	
        '''Devuelve la movilidad de un Gunpla. Se calcula según la fórmula descripta en 
        la seccion de fórmulas'''
        return self.movilidad

    def set_movilidad(self,movilidad):
        '''Determina la movilidad de un Gunpla de acuerdo al parametro recibido.'''
        self.movilidad = movilidad

    def get_armamento(self):	
        '''Devuelve una lista con todas las armas adosadas al Gunpla (Se incluyen las 
        armas disponibles en las partes)'''
        return self.armamento

    def _recibir_partes(self,partes_elegidas):
        '''Recibe las partes elegidas por el piloto, suma las estadisticas de cada parte a la del gunpla''' 
        for parte_elegida in partes_elegidas:
            if parte_elegida.tipo_de_parte == "Arma":
                 self.armamento.append(parte_elegida)
                 self.peso += parte_elegida.peso
                 self.armadura += parte_elegida.armadura
                 self.escudo += parte_elegida.escudo
                 self.energia += parte_elegida.energia
                 self.energia_restante += parte_elegida.energia
            else:
                 self.peso += parte_elegida.peso
                 self.armadura += parte_elegida.armadura
                 self.escudo += parte_elegida.escudo
                 self.velocidad += parte_elegida.velocidad
                 self.energia += parte_elegida.energia
                 self.energia_restante += parte_elegida.energia
                 if parte_elegida.armamento:
                     for arma in parte_elegida.get_armamento():
                         self.armamento.append(arma)
        self.movilidad = (self.esqueleto.movilidad - self.peso / 2 + self.velocidad * 3) / self.esqueleto.movilidad 
        if self.movilidad < 0:
            self.movilidad = 0
        elif self.movilidad > 1:
            self.movilidad = 1       

    def realizar_danio(self,piloto,arma_elegida,es_ataque_normal = True):
        '''Recibe un arma, calcula el daño que va a realizar, con una probabilidad de combinar su ataque con otras armas compatibles del arsenal(de forma recursiva)'''
        danio_total = 0
        cant_hits = arma_elegida.get_hits()
        for hit in range(cant_hits):
            precision_arma = arma_elegida.get_precision()
            if precision_arma >= random.randint(0,100):
                porcentaje_precision = precision_arma / 100
                probabilidad_danio_extra = porcentaje_precision * 0.25
                if random.randint(0,100) <= probabilidad_danio_extra:
                    print("Ha conseguido daño extra!")
                    danio_total = (arma_elegida.get_danio()) * 1.5
                else:
                    danio_total = (arma_elegida.get_danio())
        if es_ataque_normal:
            try:
                for arma in self.get_armamento():
                    if arma.esta_lista() and arma_elegida.es_combinable(arma):
                        if arma.get_tipo() == "MELEE" and random.randint(0,100) <= 40:
                            print("{} logra combinar sus armas para realizar otro ataque!!".format(piloto))
                            arma.disponible = False
                            danio_total += self.realizar_danio(piloto,arma)
                        elif arma.get_tipo() == 'RANGO' and random.randint(0,100) <= 25:
                            arma.disponible = False
                            danio_total += self.realizar_danio(piloto,arma)
            except IndexError: 
                print("Su gunpla no puede combinar ataques porque no tiene armas disponibles! ")    
        return danio_total
    
    def recibir_danio(self, danio, tipo_de_municion):
        '''Recibe el daño recibido y el tipo de municion, calcula y devuelve el daño ocasionado en el gunpla'''
        danio_ocasionado = 0
        if random.randint(0,100) <= self.movilidad * 0.8:
            danio_ocasionado = 0
        elif tipo_de_municion == "FISICA":
            danio_ocasionado = danio - self.get_armadura()
        elif tipo_de_municion == "LASER":
            danio_ocasionado = danio - danio * self.get_escudo()    
        else: 
            danio_ocasionado = danio
        if danio_ocasionado < 0:
            danio_ocasionado = 0
        self.energia_restante -= danio_ocasionado
        return danio_ocasionado          