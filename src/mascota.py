

class Persona:

   def __init__(self, nombre, tipo):
       self.__nombre = nombre
       self.__tipo = tipo


   def asignar_tipo(self, tipo):
       self.__tipo = tipo

   def asignar_nombre(self, nombre):
       self.__nombre = nombre

   def dar_tipo(self):
       return(self.__tipo)

   def dar_nombre(self):
       return(self.__nombre)