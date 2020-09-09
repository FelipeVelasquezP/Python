def main():
     Año=calcularAño()
     print("El año donde la poblacion de A sera menor que la de B es "+str(Año))
      
          



def calcularAño():
    poblacionA=35000000
    crecimientoA=1.02
    poblacionB=1990000
    CrecimientoB=1.03
    Año=2019
    i = 1
    while poblacionA>poblacionB:
       poblacionA=poblacionA*crecimientoA
       poblacionB=poblacionB*CrecimientoB
       Año=Año+1
       i += 1
    return Año

 




if __name__ == '__main__':
    main()

