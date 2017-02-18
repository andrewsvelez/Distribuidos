# -*- coding: utf-8 -*-
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

class Operaciones:
	#### servicios
	def potencia(self,x,y):
		if y==0:
			return 1
		else: 
			return self.potencia(x,y-1)*x 
	def factorial(self,n):
		if n==0:
			return 1
		else:
			return self.factorial(n-1)*n 
	def fibonacci(self,n):
		if n==0:
			return 0
		elif n==1:
			return 1
		else:
			return self.fibonacci(n-1)+self.fibonacci(n-2)
	def leertxt(self,n):
                archi=open('datos_lista.txt','r')
                linea=archi.readline()
                while linea!="":
                        print linea
                        linea=archi.readline()
                self.archi.close()

	#leer archivo y operar factorial y volver a enviarlo
	##def leerarchivo(self,n):
	#### fin de servicios
#######para iniciar el servidor
conexion=SimpleXMLRPCServer(('localhost',8000))
print "###################servidor ONLINE #####################################"
print "Soy el servidor y estoy escuchando por el puerto:" + str(8000)
conexion.register_instance(Operaciones()) 
conexion.serve_forever()


	


	
