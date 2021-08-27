def menu() ->int:

    opciones = ["Nueva carga de disciplina", "Armar medallero olimpico", "Pais con mas records mundiales",
                "Top 5 paises que mas veces subieron al podio", "Distribucion de medallas por pais"] 
    
    for opcion in range(len(opciones)):
        print(f"{opcion+1}){opciones[opcion]}")
    
    decision_usuario = int(input("\nPor favor marque la opcion deseada "))

    return decision_usuario


def cargar_nueva_disciplina(informacion_disciplinas:dict) ->None:

    nombre_disciplina_nueva = input("Introduzca el nombre de la nueva disciplina ")
    while nombre_disciplina_nueva in informacion_disciplinas:
        nombre_disciplina_nueva = input("Estas introduciendo una disciplina que ya existe, intenta nuevamente ")

    medalla_oro = input("Introduce las iniciales del pais con oro ")
    medalla_plata = input("Introduce las iniciales del pais con plata ")
    medalla_bronce = input("Introduce las iniciales del pais con bronce ")
    record_mundial = input("Marca 1 si se rompio un record mundial o 0 si no se rompio ninguno ")

    informacion_disciplinas[nombre_disciplina_nueva] = {"Oro":medalla_oro, "Plata":medalla_plata, "Bronce":medalla_bronce, "Record Mundial":record_mundial}


def reporte_records_mundiales(informacion_disciplinas:dict) ->None:

    cantidad_de_records_mundiales_por_pais = list()
    lista_paises_records_mundiales = list()

    for disciplina in informacion_disciplinas:
        if informacion_disciplinas[disciplina]['Record Mundial'] == 1:
            lista_paises_records_mundiales.append(informacion_disciplinas[disciplina]['Oro'])

    for paises_records_mundiales in lista_paises_records_mundiales:
        cantidad_de_records_mundiales_por_pais.append(lista_paises_records_mundiales.count(paises_records_mundiales))
    
    indice_maximo_ganador = cantidad_de_records_mundiales_por_pais.index(max(cantidad_de_records_mundiales_por_pais))
    print(f"El pais con mas records mundiales abatidos es: {lista_paises_records_mundiales[indice_maximo_ganador]}")


def top_cinco_podio(informacion_disciplinas:dict) ->None:

    cantidad_de_apariciones_paises = list()
    cantidad_paises = dict()
    listado_paises = list()
    for disciplina in informacion_disciplinas:
        premios = ["Oro", "Plata", "Bronce"]
        for premio in premios:
            listado_paises.append(informacion_disciplinas[disciplina][premio])
    
    for pais in listado_paises:
        cantidad_paises[pais] = {"cantidad apariciones":listado_paises.count(pais)}
    
    for cantidad_pais in cantidad_paises:
        cantidad_de_apariciones_paises.append(cantidad_paises[cantidad_pais]['cantidad apariciones'])
    claves = cantidad_paises.keys()
    cantidad_de_apariciones_paises.sort()
    cantidad_de_apariciones_paises.reverse()
    nuevo_top = cantidad_de_apariciones_paises[0:5]
    
    paises = list()
    contador = 0
    for nuevo in nuevo_top:
        for clave in claves:
            if contador < 5:
                if nuevo == cantidad_paises[clave]['cantidad apariciones']:
                    if clave not in paises:
                        paises.append(clave)
                        print(f"Pais:{clave} cantidad:{nuevo}")
                        contador+=1


def armar_podio(informacion_disciplinas:dict):

    porcentajes_ordenados = list()
    medallas_totales_juegos = list()
    medallas_paises = dict()
    paises = list()
    contador_medallas = 0
    for disciplina in informacion_disciplinas:
        premios = ["Oro","Plata","Bronce"]
        for premio in premios:
            contador_medallas+=1
            paises.append(informacion_disciplinas[disciplina][premio])
            medallas_totales_juegos.append(contador_medallas)
    for pais in paises:
        medallas_paises[pais] = {"cantidad medallas":paises.count(pais)}

    for medallas in medallas_paises:
        procentajes = (medallas_paises[medallas]['cantidad medallas'] / len(medallas_totales_juegos)) *100
        
        porcentajes_ordenados.append(procentajes)

    porcentajes_ordenados.sort()
    porcentajes_ordenados.reverse()
    contador_nuevo = 0
    for porcentaje in porcentajes_ordenados:
        for medallas in medallas_paises:
            porce = (medallas_paises[medallas]['cantidad medallas'] / len(medallas_totales_juegos)) *100
            if (medallas_paises[medallas]['cantidad medallas'] / len(medallas_totales_juegos)) *100 == porcentaje:
                if contador_nuevo != len(porcentajes_ordenados):
                    print(f"{medallas} --- {porce}")


def main() ->None:

    informacion_disciplinas = {"ciclismo":{"Oro":"GBR","Plata":"SUI","Bronce":"ESP", "Record Mundial":0},
                                "sable individual femenino":{"Oro":"ROC","Plata":"ROC","Bronce":"FRA", "Record Mundial":0},
                                "gimnasia por equipo masculino":{"Oro":"ROC","Plata":"JPN","Bronce":"CHN", "Record Mundial":0},
                                "natacion 100m mariposa femenino":{"Oro":"CAN","Plata":"CHN","Bronce":"AUS", "Record Mundial":1},
                                "natacion 100m libre masculino":{"Oro":"GBR","Plata":"NED","Bronce":"ITA", "Record Mundial":1},
                                "triatoln":{"Oro":"NOR","Plata":"GBR","Bronce":"NZL", "Record Mundial":0}}
    continuar = False
    while not continuar:
        decision_user = menu()
                                
        if decision_user == 1:
            cargar_nueva_disciplina(informacion_disciplinas)
        elif decision_user ==2:
            armar_podio(informacion_disciplinas)
        elif decision_user == 3:
            reporte_records_mundiales(informacion_disciplinas)
        elif decision_user == 4:
            top_cinco_podio(informacion_disciplinas)
        elif decision_user == 5:
            pass
        else:
            print("\nIntroduciste una opcion invalida")
        
        decision_continuar = int(input("\nMarque 1 si desea continuar o 2 si desea salir del programa "))

        if decision_continuar == 1:
            print("\nSigamos entonces")
        else:
            continuar = True
    
    print("chao")


main()
