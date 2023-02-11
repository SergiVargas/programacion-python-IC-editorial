

#Importamos la clase para poder heredar
from deportista import Deportista


#Creamos los tres tipos de deportistas
class Tenista(Deportista):
	
	def __init__ (self, nombre, edad, altura, velocidad, saque, ganados, grandes):
	
		super().__init__(nombre, edad, altura)
		self.velocidad = velocidad
		self.saque = saque
		self.ganados = ganados
		self.grandes = grandes
		
	
	def mostrar_datos(self):
		
		print ("El jugador de tenis se llama {}, tiene una edad de {} años, mide alrededor de {} cm, tiene una velocidad en pista de {} km/h y una potencia de saque de {} km/h. A lo largo de su carrera ha ganado {} partidos y {} títulos del grand slam.".format(self.nombre, self.edad, self.altura, self.velocidad, self.saque, self.ganados, self.grandes))
	


	
		
class Futbolista(Deportista):
	
	def __init__ (self, nombre, edad, altura, velocidad, seleccion, disparo, titulos):
	
		super().__init__(nombre, edad, altura)
		self.velocidad = velocidad
		self.seleccion = seleccion
		self.disparo = disparo
		self.titulos = titulos
		
		
	def mostrar_datos(self):
		
		print ("El futbolista se llama {}, tiene una edad de {} años, mide alrededor de {} cm, tiene una velocidad en carrera de {} km/h y una potencia de disparo de {} puntos. A lo largo de su carrera ha ganado {} títulos y {} juega con su selección nacional.".format(self.nombre, self.edad, self.altura, self.velocidad, self.disparo, self.titulos, self.seleccion))
		
	
	
	
	
	
	
class Ajedrecista(Deportista):
	
	def __init__ (self, nombre, edad, altura, maestro, ganadas, tablas, puntos):
	
		super().__init__(nombre, edad, altura)
		self.maestro = maestro
		self.ganadas = ganadas
		self.tablas = tablas
		self.puntos = puntos
		
	
	def mostrar_datos(self):
		
		print ("El ajedrecista se llama {}, tiene una edad de {} años, mide alrededor de {} cm. A lo largo de su carrera ha ganado {} partidas, ha hecho tablas en {} partidas, tiene {} puntos ELO y {} es un gran maestro.".format(self.nombre, self.edad, self.altura, self.ganadas, self.tablas, self.puntos, self.maestro))
		
		
	