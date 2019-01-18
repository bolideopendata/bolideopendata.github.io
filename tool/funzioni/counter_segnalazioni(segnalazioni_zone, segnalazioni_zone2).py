def counter_segnalazioni(segnalazioni_zone, segnalazioni_zone2):
    lista, new_list = [], []
    for x in segnalazioni_zone:
        var = 0
        if x not in lista:
            for y in segnalazioni_zone2:
                if x == y:
                    var = var + 1
            lista.append(x)
            new_list.append(var)
    for pos, elem in enumerate(lista):
        for pos1, elem1 in enumerate(new_list):
            if pos == pos1:
                elem.update({'Numero Segnalazioni': elem1})

    return lista
