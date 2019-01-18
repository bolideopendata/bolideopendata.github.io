def controllo_percentuale(data)
    listina, lista_prova = [], []
    for dict in data
        for x,y in dict.items()
            if 'Percentuale' in x
                listina.append(float(y))
        lista_prova.append(round(sum(listina)))
        listina = []
    return lista_prova
