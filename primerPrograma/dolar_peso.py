pesos = input("Cuantos dólares tienes?: ")
pesos = float(pesos)
valor_dolar = 20.23

total = pesos * valor_dolar
total = round(total,2)
total = str(total)

print("Tienes: $" + total + " pesos mexicanos")
