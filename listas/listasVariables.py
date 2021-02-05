def run():
    
    lista_array = ["hola", 2, 3.5, False]
    tupla = (2, 3, 5, 7, 11)

    print("Esto es una lista o array")
    for i in lista_array:
        #Esto es una lista o array. Por que además de ser mutable cuenta con datos de multiples tipos
        print(i)

    print("Y esto es una tuppla")
    for i in tupla:
        #Y esto es una tupla, ya que sus datos son inmutables y debe guardar un solo tipo de dato. En éste caso números enteros
        print(i)



if __name__ == "__main__":
    run()