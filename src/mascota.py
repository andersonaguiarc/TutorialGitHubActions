

class Persona:

   def __init__(self, nombre, tipo, dueno):
       self.__nombre = nombre
       self.__tipo = tipo
       self.__dueno = dueno


   def asignar_tipo(self, tipo):
       self.__tipo = tipo

   def asignar_nombre(self, nombre):
       self.__nombre = nombre

   def asignar_dueno(self, dueno, nombre):
       self.__dueno = dueno 
       self.__nombre = nombre

   def dar_tipo(self):
       return(self.__tipo)

   def dar_nombre(self):
       return(self.__nombre)
   
   def dar_dueno(self):
       return(self.__dueno)