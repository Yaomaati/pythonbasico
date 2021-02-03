
menu = """
Bienvenido al conversor de monedas. 💲
Elige la moneda que quieras convertir:

1.- Pesos mexicanos
2.- Pesos argentinos
3.- Pesos colombianos

 """

opcion = input(menu)
dolar_mexico = 20.23
dolar_argentina = 87.81
dolar_colombia = 3535.71

def conversion(moneda):
    peso = float(input("Cuántos pesos tienes?: "))
    dolar = peso / moneda
    dolar = round(dolar,2)
    dolar = str(dolar)
    print("Tienes: $" + dolar + " dolares")

if opcion == "1":

    conversion(dolar_mexico)
    

elif opcion == "2":

    conversion(dolar_argentina)

elif opcion == "3":

    conversion(dolar_colombia)

else:

    print("No seleccionaste ninguna opción válida")
