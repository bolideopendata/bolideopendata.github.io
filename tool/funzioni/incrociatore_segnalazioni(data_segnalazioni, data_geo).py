
def incrociatore_segnalazioni(data_segnalazioni, data_geo):
    new_dict = {}
    new_dict_list = []
    for dict in data_segnalazioni:
        for geodict in data_geo:
            if dict['Ticketid'] == geodict['Ticketid']:
                new_dict.update({'Area Statistica' : geodict['Tipo Area']})
                new_dict.update({'Categoria': dict['Category']})
                new_dict.update({'Sottocategoria': dict['Subcategory']})
                new_dict.update({'Descrizione': dict['Description']})
        if len(new_dict) > 0:
            new_dict_list.append(new_dict)
            new_dict = {}

    return new_dict_list
