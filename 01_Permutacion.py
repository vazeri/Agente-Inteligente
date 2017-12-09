from itertools import permutations, combinations 
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

print("Punto Inicial")
print(A)
print("Punto Final")
print(B)

def permutaciones(inicio, objetivo):
    perms = list(permutations(inicio)) 
    perms2 = list(combinations(A, n)) 
    if tuple(objetivo) not in perms:
			return []
    Var = perms[: perms.index(tuple(objetivo)) + 1]
    return Var
	
print("Todas las permutaciones son: \n")	
print permutaciones(A, B)
