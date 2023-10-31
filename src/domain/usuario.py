class usuario:
   def __init__(self):
      self.__nombre = None
      self.__apellido = None
      self.__mail = None
      self.__direccion = None

   def setnombre(self, nombre):
      self.__nombre = nombre

   def setapellido(self, apellido):
      self.__apellido = apellido

   def setmail(self, mail):
      self.__mail = mail
    
   def setdireccion(self, direccion):
      self.__direccion = direccion

   def datos(self):
      print ("nombre: {self.__nombre.shape}")
      print ("apellido: {self.__apellido.shape}")
      print ("mail: {self.__mail.shape}")
      print ("direccion: {self.__direccion.shape}")

