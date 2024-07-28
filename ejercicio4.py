n1 = int(input("Ingrese su primera nota: \n"))
n2 = int(input("Ingrese su segunda nota: \n"))
n3 = int(input("Ingrese su tercera nota: \n"))
n4 = int(input("Ingrese su cuarta nota: \n"))
suma = n1 + n2 + n3 + n4
promedio = suma / 4

if promedio <= 10:
    print ("F")
else:
    if promedio <= 20:
        print ("E")
    else:
        if promedio <= 30:
            print("D")
        else:
            if promedio <=40:
                print("C")
            else:
                if promedio <= 50:
                    print ("B")
                else:
                    if promedio <=100:
                        print("A")
                    else:
                        print("El total del primedio no es valido")