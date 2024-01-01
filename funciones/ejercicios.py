# 1) Definir una función con nombre numero_max() que tome como argumento 
# dos números inroducidos por el usuario y devuelva el mayor de ellos, 


# numero_uno = float(input('Escribe el primer número por favor'))
# numero_dos = float(input('Escribe el segundo numero por favor'))

# def numero_max(numero_uno,numero_dos)->float:
#     if numero_uno > numero_dos:
#         return numero_uno
#     else:
#         return numero_dos
    
# resultado=numero_max(numero_uno,numero_dos)
# print(f'El numero máximo introducido por usted es{resultado}')


# 2) Definir una función max_tres(), que tome tres números 
# como argumentos y devuelva el mayor de ellos.


# primer_numero=float(input('Escriba el primer número'))
# segundo_numero=float(input('Escriba el segundo número'))
# tercer_numero=float(input('Escriba el tercer número'))

# def max_tres(num1,num2,num3)->float:
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
    
# numero_maximo=max_tres(primer_numero,segundo_numero,tercer_numero)
# print(f'El número con el valor máximo escrito por tí es {numero_maximo}')


# 3) Escribir una funcion que tome un carácter y devuelva 
# True si es una vocal, de lo contrario devuelve Flase

# caracter=(input('Escriba una letra '))


# def vocal(caracter):
#     lista_vocales=['a','e','i','o','u']
#     if caracter in lista_vocales:
#         return True
#     else:
#         return False
    
# resultado_letra= vocal(caracter)
# print(f'Tu letra escrita es una vocal? {resultado_letra}') 



# 4) Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los numeros de una lista. 
# Por ejemplo: sum ([1,2,3,4,5]) debería devolver 10 y multiplicar ({1,2,3,4}) deberia devolver 24

# Solicitar al usuario ingresar la lista
entrada_usuario = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada del usuario a una lista de números
lista_numeros = [float(numero) for numero in entrada_usuario.split()]


def sumar(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma 


def multiplicar(lista):
    resultado=1
    for numero in lista:
        resultado*= numero
    return resultado



resultado_suma = sumar(lista_numeros)
resultado_multiplicacion = multiplicar(lista_numeros)

print(f'La suma de la lista es: {resultado_suma}')
print(f'La multiplicación de la lista es: {resultado_multiplicacion}')
