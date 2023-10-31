from controller.usuariobuilder import Builder, UsuarioBuilder
from domain.usuario import usuario

class usuarioarmado(Builder):
   
   def getnombre(self):
      nombre = nombre()
      nombre.nombre1 = "kevin"
      return nombre
   
   def getapellido(self):
      apellido = apellido()
      apellido.apellido1 = "muñoz"
      return apellido
   
   def getmail(self):
      mail = mail()
      mail.mail1 = "kevinm@gmai.com"
      return mail
   
   def getdireccion(self):
      direccion = direccion()
      direccion.direccion1 = "viamonte"
      return direccion

class nombre:
   nombre1 = None

class apellido:
   apellido1 = None

class mail:
   mail1 = None

class direccion:
   direccion1 = None

def main():
   usuarioarmado = UsuarioBuilder() 
   
   usuario1 = usuario()
   
   # Build Jeep
   print ("usuario prearmado")
   usuario1.setBuilder(usuarioarmado)
   usuario = usuario1.getusuario()
   usuario.datos()
   print ("")