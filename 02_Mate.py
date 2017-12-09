import math
print("     ____ _________  _    _  ____	")
print("    / __// __|\    \| \  / ||  __\	")
print("   / /__| |_   | |\/|  \/  || |__	")
print("  / ___/\_  \  | |  |      ||  __\	")
print(" / /__  __/ |  | |__| |\/| || |____  ")
print("/____/ /____/ /____/|_/  |_||______\ ")
print("------------------------------------ ")
print("Unidad Zacatenco, 9CV11, Practica 02")
print("------------------------------------\n")

A = (1,2,3,4)
B = (4,3,2,1)
n = len(A)		#Longitud de A

nPr = (math.factorial(n))/(math.factorial(n-n)) 	#Importa la posicion de los elementos en el grupo 
nCr = math.factorial(nPr)				#Importa la prescencia de los elementos en el grupo formado

print("\nNumero de permutaciones: %s \n" % (nPr))

print("--------------")

print ("Hay: %s! (%s) caminos distintos  \n" % (nPr,nCr))