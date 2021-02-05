def run():
    
    numero = int(input("Introduce tu número: "))

    if numero == 1:
        print("El número que elegiste NO es primo")
    else:
        for i in range(2,numero+1):
        
            if numero % i != 0:
                continue
            if numero == i:
                print("El número que elegiste SI es primo")
            else:
                print("El número que elegiste NO es primo")
                break


if __name__ == "__main__":
    run()