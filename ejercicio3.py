total = int(input("Ingrese el total de su factura \n"))
comision = total * 0.05

if total < 10000 :
    print("A usted no se le cobran comisiones")
else:
    print("El total de su factura es de", total, "por lo tanto se le cobraran", comision, "de comisión")