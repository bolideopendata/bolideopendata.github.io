def counter_segnalazioni_finale(segnalazioni_zone, segnalazioni_zone2):
    lista, new_list = [], []
    new_diz = {}
    for x in segnalazioni_zone:
        if len(new_list) == 0:
            var = 0
            for y in segnalazioni_zone2:
                if (x['Zona'] == y['Zona']) and (x['Categoria'] == y['Categoria']) and (x['Sottocategoria'] == y['Sottocategoria']):
                    var = var + int(y['Numero Segnalazioni'])
            new_diz.update(x)
            new_diz.update({'Numero Segnalazioni': var})
            lista.append(new_diz)
            new_list.append(x)
            new_diz = {}
        else:
            for z in new_list:
                if (x['Zona'] != z['Zona']) and (x['Categoria'] != z['Categoria']) and (x['Sottocategoria'] != z['Sottocategoria']):
                    var = 0
                    for y in segnalazioni_zone2:
                        if (x['Zona'] == y['Zona']) and (x['Categoria'] == y['Categoria']) and (x['Sottocategoria'] == y['Sottocategoria']):
                            var = var + int(y['Numero Segnalazioni'])
                    new_diz.update(x)
                    new_diz.update({'Numero Segnalazioni': var})
                    lista.append(new_diz)
                    new_list.append(x)
                    new_diz = {}
    return new_list
