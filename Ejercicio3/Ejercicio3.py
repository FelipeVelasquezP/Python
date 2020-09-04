
def calcularDescuento(precio,dia):
    if dia == "l":
        return precio*0.1
    elif dia == "m":
        return precio*0.05 
    elif dia == "M":
        return precio*0.03 
    elif dia == "j" or dia=="d":
        return precio*0.01 
    elif dia == "v":
        return precio*0.07 
    elif dia == "s":
        return 0
  


def main():
    precio=float(input("Ingrese el precio del producto:  "))
    if precio >0:
         dia=input("¿Que dia es hoy?   ")
         if dia=="l" or dia=="m" or dia=="M" or dia=="j" or dia=="v" or dia=="s" or dia=="d":
           Descuento=float(calcularDescuento(precio,dia))
           precioFinal=precio-Descuento
           print("El descuento es :"+str(Descuento))
           print("El precio final de producto es :"+str(precioFinal))
         else:
             print("Error, ingreso erroneo de dia");  
             main()
    else:
        print("El precio no puede ser negativo")     
        main()


if __name__ == '__main__':
    main()


