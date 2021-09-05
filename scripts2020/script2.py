class Perro(object):
	def __init__(nombre:str='',edad:int=0,raza:str=''):
		self.nombre=nombre
		self.edad=edad
		self.raza=raza.lower()

	@staticmethod
	def classify_dog(self)
		if self.raza=='beagle':
			return Beagle(self.nombre, self.edad, self.raza)
		elif self.raza=='pastor australiano':
			return PastorAustraliano(self.nombre, self.edad, self,raza)
		elif self.raza=='labrador':
			return Labrador(self.nombre, self.edad, self.raza)
		elif self.raza=='mestizo':
			return Mestizo(self.nombre, self.edad, self.raza)
		else:
			raise ValueError('No se especifico una raza valida')

class Beagle(Perro):
	def __init__(nombre, edad):
		super().__init__(nombre, edad, raza='beagle')
class PastorAustraliano(Perro):
	def __init__(nombre, edad):
		super().__init__(nombre, edad, raza='pastor australiano')
class Labrador(Perro):
	def __init__(nombre, edad):
		super().__init__(nombre, edad, raza='labrador')
class Mestizo(Perro):
	def __init__(nombre, edad):
		super().__init__(nombre, edad, raza='mestizo')
class Beagle(Perro):
	def __init__(nombre, edad):
		super().__init__(nombre, edad, raza='beagle')

if __name__ == "__main__":
	Perro1= Perro()
	Perro1.nombre=input('Nombre del perro: ')
	Perro1.edad=input('Edad del perro: ')
	Perro1.raza=input('Raza del perro: ')
