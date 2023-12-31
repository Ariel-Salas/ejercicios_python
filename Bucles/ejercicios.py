# 1) Definir una función max_tres(), que tome tres números 
# como argumentos y devuelva el mayor de ellos, realizar esta funcion con un bucle.


primer_numero=float(input('Escriba el primer número'))
segundo_numero=float(input('Escriba el segundo número'))
tercer_numero=float(input('Escriba el tercer número'))


def max_tres(num1, num2, num3):
    max_num = num1
    for num in (num2, num3):
        if num > max_num:
            max_num = num
    return max_num

result= max_tres(primer_numero,segundo_numero,tercer_numero)
print(f'El número con el valor mas alto es {result}')
