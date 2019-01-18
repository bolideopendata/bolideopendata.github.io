def diz_aree_in_zone(csv_file):
    lista_dict, new_list, lista_aree_per_zona = [], [], []
    dizionario = {}
    new_set = set()
    for dict in csv_file:
        for elem in dict:
            new_list.append(dict['NOME_ZONA'])
    for x in new_list:
        new_set.add(x)
    new_list = []
    for y in new_set:
        new_list.append(y)
    for zona in new_list:
        for dict in csv_file:
            if zona == dict['NOME_ZONA']:
                lista_aree_per_zona.append(dict['AREASTAT'])
            dizionario.update({zona : lista_aree_per_zona})
        lista_aree_per_zona = []
    return dizionario
