
menu = """
Bienvenido al conversor de monedas. 💲

1.- Pesos mexicanos
2.- Pesos argentinos
3.- Pesos colombianos

Elige que opción quieres consultar: """

opcion = input(menu)

if opcion == "1":
    pesos = input("Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    dolar_mexico = 20.23
    dolares = pesos / dolar_mexico
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes: $" + dolares + " dólares")
elif opcion == "2":
    pesos = input("Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    dolar_argentina = 87.81
    dolares = pesos / dolar_argentina
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes: $" + dolares + " dólares")
elif opcion == "3":
    pesos = input("Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    dolar_colombia = 3535.71
    dolares = pesos / dolar_colombia
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes: $" + dolares + " dólares")
else:
    print("No seleccionaste ninguna opción válida")
