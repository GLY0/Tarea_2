"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta."""

valor1 = int(input("ingrese un primer valor numerico: "))
valor2 = int(input("ingrese un segundo valor numerico: "))
while(True):
    print("""elija una opcion en el menu
    1)la suma de ambos numeros es:
    2) la resta entre ambos numeros es:
    3) la multiplicacion entre ambos numeros es: """)
    opcion= input()
    if opcion=="1":
        print("El resultado es",valor1+valor2)
    elif opcion=="2":
        print("El resultado es",valor1-valor2)
    elif opcion=="3":
        print("El resultado es",valor1*valor2)
    else:
        print("la opcion elejida no es valida")
    break 