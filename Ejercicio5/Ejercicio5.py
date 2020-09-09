def main():
        numero=int(input("Digite el nuemro limite: "))
        if numero>0:
            cadena=calcularSerie(numero)
            print(cadena)
        else:
            print("Error, Debe ser un numero positivo")
            main()
          



def calcularSerie(numero):
   cadena=""
   for x in range(numero+1):
       for y in range(x):
           cadena=cadena+str(x)
   return cadena

if __name__ == '__main__':
    main()

