def run():
    
    poblaciones = {
        "México": 127900000,
        "España": 46940000,
        "Argentina": 4449000,
        "Colombia": 49650000
    }

    #Al utilizar diccionarios, aunque no es necesario capturar los datos en forma de lista, se considera una buen práctica
    #Aquí vemos un identificador de los datos llamado "key", que sería el nombre del registro de dicho diccionario 
    #Y su información puede ser usada por "for" a través de un metodo específico para manejar diccionarios a través de las llaves o "keys"

    for i in poblaciones.keys(): #Al usar el metodo "keys" pedimos que nos devuelva el "nombre" del indice
        print(i)

    for i in poblaciones.values(): #En caso de que necesitemos conocer los valores el metodo a utilizar será "values"
        print(i)

    for i in poblaciones.items(): #Finalmente si quiero acceder a la información integra del diccionario usaré el metodo "items"
        print(i)
    
    #Al momento de utilizar "items" la manera de declarar "for" determinará el como se muestran los datos.
    #Es decir, al declarar nuestro contador, si añadimos una coma, usará el contador declarado como un identificador del diccionario.
    #Dicho de otro modo, declararemos 'pais' como un contador que leera las "keys", y 'población' como un segundo contador que arrojaran los "values".
    #Siempre y cuando estemos utilizando el metodo "items()"

    for pais, poblacion in poblaciones.items():
        
        print("La población en " + str(pais) + " es de " + str(poblacion) + " habitantes")


if __name__ == "__main__":
    run()