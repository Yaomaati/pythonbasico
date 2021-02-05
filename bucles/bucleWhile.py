def run():
    potencia = 1
    LIMITE = 1000000
    resultado = 2**potencia

    while resultado < LIMITE:

        potencia = potencia + 1
        resultado = 2**potencia
        print("La potencia de 2 elevado a " + str(potencia) + " es igual a: " + str(resultado))
        

if __name__ == "__main__":
    run()