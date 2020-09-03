class Calculo:

 def calcularEdadFutura(edad,año):
     if edad > 0 and año > 0:
        edadfutura=2070-(año-edad)
        return int(edadfutura)
     else:
        return 0
     


#  edad = int(input("Por favor ingrese la edad: "))
#  año = int(input("Por favor ingrese el año actual: "))
#  calcularEdadFutura(año,edad)
    
   
      