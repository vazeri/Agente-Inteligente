#Vazquez Gonzalez Erick
print("     ____ _________  _    _  ____	")
print("    / __// __|\    \| \  / ||  __\	")
print("   / /__| |_   | |\/|  \/  || |__	")
print("  / ___/\_  \  | |  |      ||  __\	")
print(" / /__  __/ |  | |__| |\/| || |____  ")
print("/____/ /____/ /____/|_/  |_||______\ ")
print("------------------------------------ ")
print("Unidad Zacatenco, 9CV11, Practica 02")
print("------------------------------------\n")

a = (1,2,3)
b = (3,2,1)

def combinaciones(actual):
    for i in range(len(a)-1):
        yield (actual[:i] + (actual[i+1],actual[i]) +
                   actual[i+2:])

def dfs(actual,lugar,lugar_as_set):
    lugar.append(actual)
    lugar_as_set.add(actual)
    if actual == b:
        yield lugar
    else:
        for permut_sig in combinaciones(actual):
            if permut_sig in lugar_as_set:
                continue
            for lugar in dfs(permut_sig,lugar,lugar_as_set):
                yield lugar
    lugar.pop()
    lugar_as_set.remove(actual)

for lugar in dfs(a,[],set()):

	print(lugar)
	print("--------------")

	