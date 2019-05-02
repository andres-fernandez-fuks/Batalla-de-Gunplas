from Auxiliar import Pila,Cola,LE,Nodo

from Clase_1_Gunpla import Gunpla

from Clase_2_Esqueleto import Esqueleto

from Clase_3_Parte import Parte

from Clase_4_Arma import Arma

from Clase_5_Piloto import Piloto

import random

#--------------------------------------------------------------------------------------------------------------------------------------#

# Funciones Menores: Funciones que serán utilizadas dentro las Funciones de Desarrollo del Juego para una mejor organización. Ordenandas por fases.


# Fase 1

def crear_pilotos_equipos():
	'''Devuelve una lista con los pilotos creados y una lista de listas con los equipos'''
	lista_de_pilotos = []
	equipos = []
	for i in range(1,random.choice([4,6,8])+1):
		lista_de_pilotos.append(Piloto())
		if i%2 == 0:
			equipos.append([])
	return lista_de_pilotos , equipos


def generar_lista_de_esqueletos(no_de_pilotos):
	''' 
	Función de Fase 1 (Creación del juego)
	Recibe el numero de pilotos que participan del juego.
	Devuelve una lista de los esqueletos que se podran utilizar.
	'''
	MINIMO_RANDOM = 3 # determina, junto con el número de pilotos en la partida, el número mínimo de esqueletos que se generarán para el juego
	MAXIMO_RANDOM = 6 # determina, junto con el número de pilotos en la partida, el número máximo de esqueletos que se generarán para el juego
	lista_de_esqueletos = []
	limite_inf = no_de_pilotos * MINIMO_RANDOM
	limite_sup = no_de_pilotos* MAXIMO_RANDOM
	for i in range(random.randint(limite_inf,limite_sup)):
		lista_de_esqueletos.append(Esqueleto())
	return lista_de_esqueletos


def generar_registro_partes_totales(no_de_pilotos):
	'''
	Función de Fase 1 (Creación del juego)
	Recibe el numero de pilotos del juego
	Devuelve un registro (diccionario) con el tipo de parte ("Backpack", "Arm",...) como clave y una lista aleatoria de partes como valor
	'''
	MINIMO_RANDOM = 20 # determina, junto con el número de pilotos en la partida, el número mínimo de partes que se generarán para el juego
	MAXIMO_RANDOM = 50 # determina, junto con el número de pilotos en la partida, el número máximo de partes que se generarán para el juego
	limite_inf = no_de_pilotos * MINIMO_RANDOM
	limite_sup = no_de_pilotos * MAXIMO_RANDOM
	registro = {}
	for j in range(random.randint(limite_inf,limite_sup)):
		if random.randint(0,1) == 0:
			parte = Arma()
		else:
			parte = Parte()
			agregar_armas_a_parte(parte)
		tipo = parte.get_tipo_parte()
		registro[tipo] = registro.get(tipo,Pila())
		registro[tipo].apilar(parte)
	return registro


def agregar_armas_a_parte(parte):
	'''
	Función auxiliar para la creación de partes:
	Recibe una parte y le agrega un conjunto aleatorio de armas
	'''
	armas = []
	for i in range(probabilidad_de_arma(parte)):
		armas.append(Arma())
	parte._definir_armamento(armas)
		 

def probabilidad_de_arma(parte):
	'''
	Función auxiliar para agregar un arma a una parte.
	Recibe una parte y devuelve el número de armas que se agregarán a la parte.
	'''
	if parte.get_tipo_parte() == 'Head' or parte.get_tipo_parte() == 'Leg':
		return random.randint(0,1)
	else:
		return random.randint(1,3)


def elegir_piezas(registro_origen,registro_destino,ronda_de_pilotos):
	'''
	Función específica para la elección de partes y de armas por parte de los pilotos (se usa en la Fase 2)
	Recibe dos registros (diccionarios), uno con las piezas disponibles y otro vacío, además de una ronda de pilotos.
	Completa el segundo registro con los pilotos como clave y una lista de piezas reservadas para cada uno como valor.
	'''
	while registro_origen:
		'''for tipo_de_parte in list(registro_origen.values()): #para imprimir lo que ven los pilotos en las pilas
			if not tipo_de_parte.esta_vacia():
				#print(tipo_de_parte.ver_ultimo())'''
		piloto = ronda_de_pilotos.desencolar()
		tipo_de_pieza = piloto.elegir_parte(registro_origen)
		try:
			pieza_elegida = registro_origen[tipo_de_pieza].desapilar()
			print("El piloto {} reserva {}".format(piloto.nombre, repr(pieza_elegida)))
			registro_destino[piloto] = registro_destino.get(piloto,[]) + [pieza_elegida]
		except IndexError:
			registro_origen.pop(tipo_de_pieza)
		finally:
			ronda_de_pilotos.encolar(piloto)

def swap(lista_de_pilotos, pos1, pos2):
	'''Recibe una lista y dos posiciones.Intercambia la posicion de esos elementos'''
	lista_de_pilotos[pos1], lista_de_pilotos[pos2] = lista_de_pilotos[pos2], lista_de_pilotos[pos1]


def posicion_maximo(lista_de_pilotos, largo):
	'''Recibe una lista y el largo de esa lista. Devuelve la posicion del máximo valor(velocidad)'''
	max_pos = 0
	for i in range(largo):
		if lista_de_pilotos[i].gunpla.get_velocidad()> lista_de_pilotos[max_pos].gunpla.get_velocidad():
			max_pos = i
	return max_pos


def seleccion(lista_de_pilotos):
	'''Recibe una lista, la ordena de mayor a menor segun la velocidad, mediante el metodo de seleccion'''
	for i in range(len(lista_de_pilotos)):
		pos_max = posicion_maximo(lista_de_pilotos, len(lista_de_pilotos) - i)
		swap(lista_de_pilotos, pos_max, len(lista_de_pilotos) - i - 1)
	return lista_de_pilotos


def asignar_equipo(piloto, equipos,no_de_pilotos):
	'''Recibe un piloto y una lista de equipos y el numero de pilotos. Asigna el piloto a un equipo, modificando la lista equipos'''
	equipo_posible = random.randint(0, (no_de_pilotos/2) - 1)
	while len(equipos[equipo_posible])>1:
		equipo_posible = random.randint(0, (no_de_pilotos/2) - 1)
	equipos[equipo_posible].append(piloto)	


def asignar_esqueletos_gunplas(lista_de_pilotos,lista_de_esqueletos):
	'''Recibe una lista de pilotos y una lista de esqueletos, Asigna a cada piloto un gunpla con el esqueleto deseado'''
	for piloto in lista_de_pilotos: 
		esqueleto = lista_de_esqueletos[piloto.elegir_esqueleto(lista_de_esqueletos)]
		gunpla = Gunpla(esqueleto)
		piloto.set__Gunpla_(gunpla)
		print("EL piloto {} utilizará al {}".format(piloto.nombre , piloto.gunpla.nombre))


def elegir_oponente(piloto,oponentes,equipos):
	''' Recibe una instancia de Piloto, una lista de oponentes y otra de equipos.
		Elige y devuelve una instancia de Piloto (oponente).
	'''
	oponentes = calcular_posibles_objetivos(piloto, equipos)	
	oponente_elegido = piloto.elegir_oponente(oponentes) 
	oponente = oponentes[oponente_elegido]
	return oponente	

def determinar_impresion_ataque(danio_ocasionado,ronda,oponente):
	''' Recibe un valor númerico (daño ocasionado), una instancia de Cola (ronda) y una de Piloto (oponente)
		Imprime por pantalla de acuerdo al valor recibido, y puede o no modificar la ronda.
	'''
	if danio_ocasionado > 0:
		print("Le ha causado {} de daño al gunpla enemigo!(Energia restante: {})".format	(danio_ocasionado,oponente.gunpla.get_energia_restante()))
	else:
		print("¡No le ha causado daño!, ¡{} consigue un turno extra en la proxima ronda!".format(oponente))
		ronda.encolar(oponente)


def determinar_impresion_contraataque(danio_ocasionado,piloto,oponente):
	''' Recibe un valor númerico (daño ocasionado) y dos instancias de Piloto.
		Imprime por pantalla de acuerdo al valor recibido.
	'''
	if danio_ocasionado > 0:
		print("Causandole {} de daño al gunpla enemigo!(Energia restante: {})".format	(danio_ocasionado,piloto.gunpla.get_energia_restante()))
	elif danio_ocasionado == 0 :
		print("¡No le ha causado daño!")
	else:
		print("Su ataque ha terminado recargando la energia del gunpla de {}".format(oponente))
	if piloto.gunpla.get_energia_restante() <= 0:
		print("¡Por lo tanto, el piloto {} ha terminado siendo destruido!".format(piloto))

		
def  calcular_posibles_objetivos(piloto, equipos):
	'''Recibe un piloto y la lista de equipos. Calcula y devuelve una lista de oponentes activos para ese piloto'''
	oponentes = []
	for equipo in equipos:
		if not piloto in equipo:
			for oponente in equipo:
				if oponente.gunpla.get_energia_restante() >0:
					oponentes.append(oponente)
	return oponentes	

def declarar_victoria(piloto, equipos): #para ver quien gana
	'''Recibe un piloto y la lista de equipos. Declara(imprime) si un equipo gano el combate'''
	for i, equipo in list(enumerate(equipos)):
		if piloto in equipo:
			print("\n----Al equipo {} no le quedaron mas enemigos----\n".format(i+1))
			print("---Ganadores--")
			for ganador in equipo:
				print("---{}".format(ganador),end="---")
				if ganador.gunpla.get_energia_restante() < 0:
					print("(Sin energia)") 
				print()




#--------------------------------------------------------------------------------------------------------------------------------------#

# Funciones del Desarrollo del Juego: Agrupan las funciones menores para organizar el Desarrollo del Juego

def _DdJ_1_armar_equipos():
	''' No recibe parámetros. Crea y devuelve una lista de pilotos, el número de pilotos y los equipos en los que se organizarán.''' 
	lista_de_nombres_libres = ["Setsuna F. Seiei","Heero Yuy","Ayame","Kira Yamato","Tsukasa Shiba","Duo Maxwell","Trowa Barton","Quatre Raberba Winner"]#para 	ver quien es quien
	lista_de_pilotos , equipos = crear_pilotos_equipos()
	no_de_pilotos = len(lista_de_pilotos)
	for piloto in lista_de_pilotos:
		while not piloto.nombre:
			nombre = random.choice(lista_de_nombres_libres)
			lista_de_nombres_libres.remove(nombre)
			piloto.nombre = nombre
		asignar_equipo(piloto, equipos, no_de_pilotos)
		print("Ha llegado {}".format(piloto.nombre))
	for equipo in equipos:
		print("Se ha formado el equipo: ")
		for piloto in equipo:
			 print("--{}".format(piloto))
	return lista_de_pilotos,no_de_pilotos, equipos

def _DdJ_1_creacion_y_eleccion_de_partes(lista_de_pilotos,no_de_pilotos):
	''' Recibe el número de pilotos de la partida.
		Crea y devuelve los instrumentos para los pilotos: una lista de esqueletos, y dos diccionarios, uno con partes y otro con armas'''
	lista_de_esqueletos = generar_lista_de_esqueletos(no_de_pilotos)	
	registro_partes_totales = generar_registro_partes_totales(no_de_pilotos)
	ronda_de_eleccion = Cola()
	asignar_esqueletos_gunplas(lista_de_pilotos,lista_de_esqueletos)
	for i in range(no_de_pilotos):
		ronda_de_eleccion.encolar(lista_de_pilotos.pop(random.randint(0,len(lista_de_pilotos)-1)))
	registro_partes_reservadas = {} # Diccionario donde se guardara la información sobre las partes reservadas por piloto
	registro_armas_reservadas = {} # Diccionario donde se guardara la información sobre las armas reservadas por piloto
	elegir_piezas(registro_partes_totales,registro_partes_reservadas,ronda_de_eleccion)
	print()
	return ronda_de_eleccion,registro_partes_reservadas,registro_armas_reservadas

def _DdJ_1_combinar_partes(ronda,registro_partes_reservadas,registro_armas_reservadas,lista_de_pilotos):
	''' Recibe una instancia de Cola (ronda) que contiene Pilotos, dos diccionarios con partes y armas reservadas y una lista de pilotos.
		No devuelve nada, modifica algunos atributos de los Pilotos de la ronda (les asigna armas y partes).
	'''
	i = 0
	while not ronda.esta_vacia():
		piloto = ronda.desencolar()
		i += 1
		print("El piloto {} esta eligiendo sus partes".format(piloto)) 
		partes_elegidas = piloto.elegir_combinacion(registro_partes_reservadas[piloto])
		gunpla = piloto.get__Gunpla_()       
		gunpla._recibir_partes(partes_elegidas)
		lista_de_pilotos.append(piloto)


def _DdJ_2_continuar_juego(piloto,equipos,oponentes):
	''' Recibe una instancia de Piloto, una lista de equipos y otra de oponentes.
		Devuelve un valor booleano que determina si continuar o no con la partida.
	'''
	if len(oponentes) == 0 and piloto.gunpla.get_energia_restante() > 0 :
		declarar_victoria(piloto, equipos)
		return False
	return True


def _DdJ_2_turno_de_ataque(ronda,piloto,oponentes,equipos):
	'''
	Recibe una instancia de Cola (ronda), una de Piloto, una lista de oponentes y otra con equipos.
	Devuelve una instancia de Arma (el arma elegida para atacar) y una instancia de Piloto (el oponente).
	'''
	oponente = elegir_oponente(piloto,oponentes,equipos)
	try:
		arma_para_atacar = piloto.elegir_arma(oponente)
		print("EL piloto {} ataca a {} con {}".format(piloto, oponente, arma_para_atacar.get_clase()))
		danio = piloto.get__Gunpla_().realizar_danio(piloto,arma_para_atacar)
		municion = arma_para_atacar.get_tipo_municion()
		danio_ocasionado = oponente.get__Gunpla_().recibir_danio(danio, municion)
		determinar_impresion_ataque(danio_ocasionado,ronda,oponente)
		return arma_para_atacar,oponente
	except IndexError:
		print("{} no puede atacar: su gunpla no cuenta con suficiente armamento".format(piloto))



def _DdJ_2_preparacion(lista_de_pilotos):
	'''
	Recibe una lista de pilotos
	Imprime por pantalla el inicio de la pelea y devuelve una Instancia de Cola (ronda de combate)
	'''
	ronda_de_combate = Cola()
	lista_de_pilotos = seleccion(lista_de_pilotos)
	print("Los pilotos estan listos!")
	n_de_combatientes = len(lista_de_pilotos)
	for i in range(n_de_combatientes):
		piloto = lista_de_pilotos[i]
		print(repr(piloto))
		ronda_de_combate.encolar(piloto)
	print("¡FIGHT!")
	return ronda_de_combate


def _DdJ_2_resultado_de_ataque(ronda,oponente,arma,piloto):
	'''
	Recibe dos Instancias de Piloto, una de Arma y una de Cola(ronda).
	Simula un ataque, pudiendo o no modificar los atributos de las instancias, y devuelve un valor booleano de si existe o no un contraataque.
	'''
	contraataque = False
	if oponente.gunpla.get_energia_restante() <= 0:
		print("EL oponente {} ha sido destruido".format(oponente))
		if abs(oponente.gunpla.get_energia_restante()) > oponente.gunpla.get_energia() * 0.05:
			print("Overkill! El piloto {} consigue un turno extra en la proxima ronda!.".format(piloto))
			ronda.encolar(piloto)
	elif arma and arma.get_tipo() == "MELEE":
		print("{} contraataca!".format(oponente))
		contraataque = True
	elif arma.get_tipo() == "RANGO":
		print("El arma utilizada fue un arma de Rango. No hay contraataque.")
	return contraataque


def _DdJ_2_contraataque(piloto,oponente,arma):
	'''
	Recibe dos Instancias de Piloto y una de Arma.
	Simula un contraataque, pudiendo o no modificar los atributos de las instancias
	'''
	try:
		arma = oponente.elegir_arma(piloto)
		municion = arma.get_tipo_municion()
		danio = oponente.get__Gunpla_().realizar_danio(oponente,arma,False)
		danio_ocasionado = piloto.get__Gunpla_().recibir_danio(danio, municion)
		determinar_impresion_contraataque(danio_ocasionado,piloto,oponente)
	except IndexError:
		print("{} no puede atacar: su gunpla no cuenta con suficiente armamento.".format(oponente))


def _DdJ_2_simular_pelea(ronda_de_combate,equipos,lista_de_pilotos):
	''' Recibe una Ronda de Combate en forma de Cola, una lista de equipos y una lista de pilotos
		No devuelve nada, imprime por pantalla el estado de la partida hasta que termina.
	'''
	i=0
	while not ronda_de_combate.esta_vacia():
		piloto = ronda_de_combate.desencolar()
		oponentes = calcular_posibles_objetivos(piloto, equipos)
		if _DdJ_2_continuar_juego(piloto,equipos,oponentes):
			i += 1
			if piloto.gunpla.get_energia_restante() > 0:
				print('\nTurno ' + str(i))
				try:
					arma_para_atacar, oponente = _DdJ_2_turno_de_ataque(ronda_de_combate,piloto,oponentes,equipos)
					contraataque = _DdJ_2_resultado_de_ataque(ronda_de_combate,oponente,arma_para_atacar,piloto)
					if contraataque:
						_DdJ_2_contraataque(piloto,oponente,arma_para_atacar)				
				except TypeError:
					print("EL piloto {} no cuenta con el armamento suficiente para atacar en este turno.".format(piloto))
				finally:
					ronda_de_combate.encolar(piloto)
		else:
			break





#--------------------------------------------------------------------------------------------------------------------------------------#

def main():

	# Fase 1: Creacion de Pilotos y Equipos y Eleccion de Esqueletos, Armas y Partes

	lista_de_pilotos,no_de_pilotos, equipos = _DdJ_1_armar_equipos()

	ronda_de_eleccion,registro_partes_reservadas,registro_armas_reservadas = _DdJ_1_creacion_y_eleccion_de_partes(lista_de_pilotos,no_de_pilotos)

	_DdJ_1_combinar_partes(ronda_de_eleccion,registro_partes_reservadas,registro_armas_reservadas,lista_de_pilotos)

	# Fase 2: Combate

	ronda_de_combate = _DdJ_2_preparacion(lista_de_pilotos)

	_DdJ_2_simular_pelea(ronda_de_combate,equipos,lista_de_pilotos)
	

main()
