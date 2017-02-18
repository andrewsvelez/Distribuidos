import xmlrpclib
import os
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
def menu():
	print "##############BIENVENIDOS AL MENU ARITMETICO#####################"
	print "			1. POTENCIA"
	print "			2. FACTORIAL"
	print "			3. SERIE DE FIBONACCI"
	print "			4. LLENAR LISTA/TUPLA"
	print "			0. SALIR"
	
def crear_archivo():        
	archivo = "datos_lista.txt"
	arch = open(archivo,'w')
	dato = str(input("Dígame un número: "))
	arch.write(dato)
	arch.close()
	return archivo
	

def conectar():
	menu()
	a=input('Ingrese una opcion: ')
	if a==1:	
		os.system('cls')
		b=input('Ingrese la base: ')
		c=input('Ingrese el exponente: ')
		print "El valor de la potencia es : "+str(proxy.potencia(b,c))
	elif a==2:
		os.system('cls')
		n=input("ingrese un entero: ")
		print "el factorial de : "+str(n)+str("es: ")+str(proxy.factorial(n))
	elif a==3:
		os.system('cls')
		n=input("ingrese un entero: ")
		print "el numero de fibonacci es: "+str(proxy.fibonacci(n))
	elif a==4:
		os.system('cls')
		#dato=input("ingrese un valor: ")
		n=crear_archivo()
		print "el numero de fact es: "+str(proxy.leertxt(n))
		#print "te toca implementarla"		
                	
	elif a==0:
		print "para el servidor y todo el equipo fue un placer atenderle, regresa pronto a nuestro MENU"
		exit()

conectar()


