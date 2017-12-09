#Vazquez Gonzalez Erick
print("     ____ _________  _    _  ____	")
print("    / __// __|\    \| \  / ||  __\	")
print("   / /__| |_   | |\/|  \/  || |__	")
print("  / ___/\_  \  | |  |      ||  __\	")
print(" / /__  __/ |  | |__| |\/| || |____  ")
print("/____/ /____/ /____/|_/  |_||______\ ")
print("------------------------------------ ")
print("ESIME Unidad Zacatenco, 9CV11, Caminos")
print("------------------------------------\n")

a = (1,2,3,4)
b = (4,3,2,1)

def combinaciones(actual):
    for i in range(len(a)-1):
        yield (actual[:i] + (actual[i+1],actual[i]) +
                   actual[i+2:])

def Intercambio(actual,lugar,punto_final):
    lugar.append(actual)
    punto_final.add(actual)
    if actual == b:
        yield lugar
    else:
        for permut_sig in combinaciones(actual):
            if permut_sig in punto_final:
                continue
            for lugar in Intercambio(permut_sig,lugar,punto_final):
                yield lugar
    lugar.pop()
    punto_final.remove(actual)

for lugar in Intercambio(a,[],set()):

	print(lugar)
	print("--------------")

	