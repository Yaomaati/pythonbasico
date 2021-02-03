
menu = """
Bienvenido al conversor de monedas. 💲
Elige la moneda que quieras consultar:

1.- Pesos mexicanos
2.- Pesos argentinos
3.- Pesos colombianos

 """

opcion = input(menu)
dolar_mexico = 20.23
dolar_argentina = 87.81
dolar_colombia = 3535.71

def conversion(moneda, pais):
    dolares = input("Cuántos dolares tienes?: ")
    dolares = float(dolares)
    pesos = dolares * moneda
    pesos = round(pesos,2)
    pesos = str(pesos)
    print("Tienes: $" + pesos + pais)

if opcion == "1":

    conversion(dolar_mexico, " pesos mexicanos")
    

elif opcion == "2":

    conversion(dolar_argentina, " pesos argentinos")

elif opcion == "3":

    conversion(dolar_colombia, " pesos colombianos")

else:

    print("No seleccionaste ninguna opción válida")
