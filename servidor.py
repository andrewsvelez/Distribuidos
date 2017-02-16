import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
def suma_remota(a,b):
    return a+b


puerto=input("ingrese el puerto: ")
#se crea el servidor
conexion = SimpleXMLRPCServer(("localhost",puerto))
print "amigo soy el servidor... escuchando por el "+ str(puerto)
conexion.register_function(suma_remota,"suma")
# se lanza el servidor
conexion.serve_forever()
