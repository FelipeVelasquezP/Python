
      
def calcularEdadFutura(año,edad):
     if edad > 0 and año > 0:
        edadfutura=2070-(año-edad)
        return int(edadfutura)
     else:
        return 0


def main():
   edad = int(input("Por favor ingrese la edad: "))
   año = int(input("Por favor ingrese el año actual: "))
   edadFutura=str(calcularEdadFutura(año,edad))
   print("Su Edad en el 2070 sera: "+edadFutura)



main()



