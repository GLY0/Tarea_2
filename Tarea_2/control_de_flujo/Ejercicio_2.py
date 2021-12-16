""" Realiza un programa que lea un número impar por teclado. Si el usuario no introduce 
un número impar, debe repetise el proceso hasta que lo introduzca correctamente."""

valor1 = int(input("ingrese un numero impar"))

while(True):
    valor1=valor1%2
    if valor1==0:
        print("intentelo nuevamente")
        valor1 = int(input("ingrese un numero impar")) 
    else:
        print("su numero es impar")
        break