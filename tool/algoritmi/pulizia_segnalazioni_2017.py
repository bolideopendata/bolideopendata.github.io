import pandas


def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(x) for x in reader]
    return data

def process_data_punto_e_virgola(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        data = [dict(x) for x in reader]
    return data

def pulitore_data_geo(data_geo):
    dict_list_pulita = []
    dict_pulito = {}
    for dict in data_geo:
        dict_pulito.update({'Ticketid': dict['TICKETID']})
        for x, y in dict.items():
            if x == 'TIPO_AREA_':
                if 'Area Statistica: ' in y:
                    newy = y.replace("Area Statistica: ", '')
                    dict_pulito.update({'Tipo Area': newy})
                elif 'Percorso di ascolto |' in y:
                    newy = y.replace('Percorso di ascolto | ', '')
                    dict_pulito.update({'Tipo Area': newy})
        dict_list_pulita.append(dict_pulito)
        dict_pulito = {}

    df = pandas.DataFrame(dict_list_pulita)
    df.to_csv('Segnalazioni_file_per_merge.csv', columns=['Ticketid', 'Tipo Area'], sep=',', encoding='utf-8',  index=False)
    return dict_list_pulita

def pulire_segnalazioni(data_segnalazioni):
    data_segnalazioni[:] = [dict for dict in data_segnalazioni if dict.get('Category') == 'Degrado ambientale' or dict.get('Category') =='Degrado sociale' or dict.get('Category') == 'Microcriminalita']
    return data_segnalazioni

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


def delete_descrizione(data):
    lista = []
    new_dict = {}
    for row in data:
        if row['Sottocategoria'] == 'Segnalazioni':
            new_dict.update({'Zona': row['Zona']})
            new_dict.update({'Categoria': row['Categoria']})
            new_dict.update({'Sottocategoria': row['Descrizione']})
            new_dict.update({'Numero Segnalazioni': row['Numero Segnalazioni']})
            lista.append(new_dict)
            new_dict = {}
        else:
            new_dict.update({'Zona': row['Zona']})
            new_dict.update({'Categoria': row['Categoria']})
            new_dict.update({'Sottocategoria': row['Sottocategoria']})
            new_dict.update({'Numero Segnalazioni': row['Numero Segnalazioni']})
            lista.append(new_dict)
            new_dict = {}
    return data

def sottocat_in_altro(data):
    lista = []
    new_dict = {}
    for row in data:
        if row['Sottocategoria'] == ' ' or row['Sottocategoria'] == '':
            new_dict.update({'Zona': row['Zona']})
            new_dict.update({'Categoria': row['Categoria']})
            new_dict.update({'Sottocategoria': 'Altro'})
            new_dict.update({'Numero Segnalazioni': row['Numero Segnalazioni']})
            lista.append(new_dict)
            new_dict = {}
        else:
            new_dict.update({'Zona': row['Zona']})
            new_dict.update({'Categoria': row['Categoria']})
            new_dict.update({'Sottocategoria': row['Sottocategoria']})
            new_dict.update({'Numero Segnalazioni': row['Numero Segnalazioni']})
            lista.append(new_dict)
            new_dict = {}

    return data

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
