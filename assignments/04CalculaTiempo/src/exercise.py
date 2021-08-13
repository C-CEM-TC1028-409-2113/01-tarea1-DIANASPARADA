def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Dame tu edad: "))
    año = int(input("Dame el año actual: "))
    edad_2 = ( 100 - edad ) + año 
    print("Cumplirás 100 años en el año:",edad_2)

if __name__ == '__main__':
    main()