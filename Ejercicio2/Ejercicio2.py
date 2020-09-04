def main():
        numero=input("Digite un numero: ")
        try:           
                bandera=validarNumero(int(numero))
                if bandera:
                     print("El numero si es par")
                else:
                     print("¡Falso! El numero es Impar")
                main()
        except ValueError:
                print("Erro Inrese los datos correctamete")
                main()
      
          



def validarNumero(numero):
    return(bool(numero % 2==0))


if __name__ == '__main__':
    main()

