def segnalazioni_per_zone(diz_zone_aree, segnalazioni_aree):
    new_dict = {}
    lista = []
    for key,value in diz_zone_aree.items():
        for z in value:
            for diz in segnalazioni_aree:
                for x,y in diz.items():
                    if z == y:
                        new_dict.update({'Zona': key})
                        new_dict.update({'Categoria': diz['Categoria']})
                        new_dict.update({'Sottocategoria': diz['Sottocategoria']})
                        new_dict.update({'Descrizione': diz['Descrizione']})
                        lista.append(new_dict)
                        new_dict = {}

    return lista
