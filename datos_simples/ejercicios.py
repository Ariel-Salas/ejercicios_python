# Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.


horas = float(input("Escribe tus horas trabajadas mensuales: "))
costo = float(input("Escribe cuántos dinero en CLP vale tu hora "))

def total(horas:float, costo: float):
    pagar= horas*costo
    return pagar

total_pagar=total(horas,costo)
print(f'Tu pago mensual será de: {total_pagar}')

