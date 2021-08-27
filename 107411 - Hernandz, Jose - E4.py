def obteniendo_y_operando_numeros(numeros:str) ->tuple:

    lista_numeros_enteros = list()
    lista_nueva = numeros.split()
    
    for numero in lista_nueva:
        lista_numeros_enteros.append(int(numero))
    
    numero_maximo = max(lista_numeros_enteros)
    numero_minimo = min(lista_numeros_enteros)
    sumatoria_total_numeros = sum(lista_numeros_enteros)

    return (numero_maximo, numero_minimo, sumatoria_total_numeros)


def main():

    numeros = input("Introduce los numeros separados por espacios ")
    clasificacion_de_numeros = obteniendo_y_operando_numeros(numeros)
    print(clasificacion_de_numeros)


main()
