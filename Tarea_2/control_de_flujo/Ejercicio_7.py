lista1 = ["1","9","3","0","5","6","7","8"]
lista2 = ["1","6","9"]
lista3 = []
print(lista1)
print(lista2)

for numero in lista1:
    if numero in lista2 and numero not in lista3:
        lista3.append(numero)

print(lista3)
        