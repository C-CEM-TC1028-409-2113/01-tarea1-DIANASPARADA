def main():
    #escribe tu código abajo de esta línea
    año_1 = float(input("Dame el año de nacimiento: "))
    año_2 = float(input("Dame el año actual: "))
    lustros  = (año_2 - año_1)/5
    print("Los lustros que has vivido son:", lustros)

if __name__ == '__main__':
    main()