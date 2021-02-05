import random

def run():

    num_aleatorio = random.randint(1, 100)
    usuario = int(input("Tienes 5 oportunidades para adivinar el número del 1 al 100:"))
    vidas = 4

    while num_aleatorio != usuario and vidas > 0:

        if usuario > num_aleatorio:
            print("Es mas pequeño, te quedan: " + str(vidas) + " vidas")
            vidas -= 1                
        elif usuario < num_aleatorio:
            print("Es mas grande, te quedan: " + str(vidas) + " vidas")
            vidas -= 1
        elif vidas == 0:
            break
        usuario = int(input("Elige otro número:"))
    if num_aleatorio == usuario:
        print("Ganaste")
    else:
        print("Perdiste")

if __name__ == "__main__":
    run()