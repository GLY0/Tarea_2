""" Realiza un programa que pida al usuario cuantos números quiere 
introducir. Luego lee todos los números y realiza una media aritmética:"""

sumatoria = 0
n = int(input("¿Cuántos números quieres introducir? ") )
for M in range(n):
    sumatoria += float(input("Introduce un número: ") )
print(" la media aritmetica entre los valores introducidos es: ",sumatoria/n)