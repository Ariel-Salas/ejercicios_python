# Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.


horas = float(input("Escribe tus horas trabajadas mensuales: "))
costo = float(input("Escribe cuántos dinero en CLP vale tu hora "))

def total(horas:float, costo: float):
    pagar= horas*costo
    return pagar

total_pagar=total(horas,costo)
print(f'Tu pago mensual será de: {total_pagar}')

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
# es el índice de masa corporal calculado redondeado con dos decimales.

peso=float(input('Esribe tu peso en kilos por favor'))
estatura=float(input('Escribe tu estatura en metros por favor'))


def calcular_imc(peso,estatura)->float:
    imc= round(peso/(estatura**2),3)
    return imc

imc=calcular_imc(peso,estatura)
print(f'Tu indice de masa corporal es {imc}')

