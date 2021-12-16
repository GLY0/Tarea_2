"""Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:"""
def pares_impares(lista):
    pares = []
    impares = []
    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares
lista = [3, 8, 2, 6, 7, 1, 0, 10, 9, 11, 15, 5]
pares, impares = pares_impares(lista)
print("Pares: ", pares)
print("Impares: ", impares)