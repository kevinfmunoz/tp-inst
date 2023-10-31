class UsuarioBuilder:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def builderusuario(self):
      
      usuario = usuario()
      
      nombre = self.__builder.getnombre()
      usuario.setnombre(nombre)
      
      apellido = self.__builder.getapellido()
      usuario.setapellido(apellido)

      mail = self.__builder.getmail()
      usuario.setmail(mail)

      direccion = self.__builder.getdireccion()
      usuario.setdireccion(direccion)

      return usuario

class Builder:
      def getnombre(self): 
         pass
      def getapellido(self): 
         pass
      def getmail(self): 
         pass
      def getdireccion(self): 
         pass