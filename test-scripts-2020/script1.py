class Persona: #si lo dejas así, se sobre entiende: class Persona(object)
	def __init__(self, nombre:str, edad:int, coreano:bool=False) -> None:
		self.nombre = nombre
		self.edad = edad + 1 if coreano else edad
#		if coreano:
#			self.edad=edad+1
#		else:
#			self.edad=edad
	def presenta(self):
		print(f"Hola, mi nombre es {self.nombre}.")
	def correr(self):
		print("Lo siento, estoy corriendo")
	def saluda(self, otra_persona):
		print(f"Hola, {otra_persona.nombre}")

class Genomico(Persona):
	def __init__(self, nombre:str, edad:int) -> None:
		super().__init__(nombre,edad,coreano=False)
	def saluda(self, otro_genomico):
		print("beso o queso?")
	#def __init_subclass__(cls)
class Perro(object):
	pass


if __name__ == "__main__":
	David=Persona(nombre="David", edad=21)
	David.correr()

	Jesús=Persona(nombre="Jesús", edad=22)
	Christian=Persona(nombre="Christian", edad=28, coreano=True)
#	Jesús.saluda(David)
#	David.saluda(Jesús)
	genomico1=Genomico("Alex",20)
	genomico2=Genomico("Kevin",20)

	genomico1.saluda(genomico2)
	print(type(genomico1))
