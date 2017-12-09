#Vazquez Gonzalez Erick
#https://docs.python.org/2/library/itertools.html#itertools.permutations
from itertools import permutations, combinations 
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

A = (1,2,3)
B = (3,2,1)
n = len(A)		#Longitud de A

nPr = (math.factorial(n))/(math.factorial(n-n)) 	#Importa la posicion de los elementos en el grupo 
#nCr = math.factorial(nPr)				#Importa la prescencia de los elementos en el grupo formado


print("Punto Inicial")
print(A)
print("Punto Final")
print(B)
print("\nNumero de permutaciones: %s \n" % (nPr))

def permutaciones(inicio, objetivo):
    perms = list(permutations(inicio)) 
    perms2 = list(combinations(A, n)) 
    if tuple(objetivo) not in perms:
			return []
    Var = perms[: perms.index(tuple(objetivo)) + 1]
    return Var
	
print permutaciones(A, B)
print("--------------")

#print ("Hay: %s! (%s) caminos distintos  \n" % (nPr,nCr))

raw_input("Desea ver todos los caminos posibles? (enter) \n") 

#Programa 3

a = A
b = B

def children(actual):
    for i in range(len(a)-1):
        yield (actual[:i] + (actual[i+1],actual[i]) +
                   actual[i+2:])

def dfs(actual,lugar,lugar_as_set):
    lugar.append(actual)
    lugar_as_set.add(actual)
    if actual == b:
        yield lugar
    else:
        for permut_sig in children(actual):
            if permut_sig in lugar_as_set:
                continue
            for lugar in dfs(permut_sig,lugar,lugar_as_set):
                yield lugar
    lugar.pop()
    lugar_as_set.remove(actual)

for lugar in dfs(a,[],set()):

	print(lugar)
	print("--------------")

	