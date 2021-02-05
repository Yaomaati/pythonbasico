def run():

    potencia = 0
    resultado = 2**potencia

    while resultado <= 1000000000:
        print(resultado)
        potencia += 1
        resultado = 2**potencia

        if resultado >= 250000000:
            break
        elif resultado % 2 != 0:
            continue


if __name__ == "__main__":
    run()