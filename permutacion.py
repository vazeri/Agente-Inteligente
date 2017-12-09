#Vazquez Gonzalez Erick
#https://docs.python.org/2/library/itertools.html#itertools.permutations

from itertools import permutations
import math

A = ([1,2,3])
B = ([3,2,1])
n = len(A)	#Longitud de A

print("ORIGINAL")
print(A)
print("FINAL")
print(B)
print("Permutaciones:")
print("--------------")
def combinaciones(inicio, objetivo):
    perms = list(permutations(inicio)) #Long del vector
    #all_perms = list(permutations(sorted(inicio), len(inicio))) #Long del vector
    if tuple(objetivo) not in perms:
        # regresa una lista vacia si no se encuentra el apuntador final en todas las permutaciones
        return []
	Var = perms[: perms.index(tuple(objetivo)) + 1]
    return Var
	
nPr= math.factorial(n)/math.factorial(n-2) #Formula de permutacion
print combinaciones(A, B)
print("--------------")
print("\nManeras distintas de llegar al mismo resultado:")
print nPr 