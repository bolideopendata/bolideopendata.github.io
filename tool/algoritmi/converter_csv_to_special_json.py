
lista_zone = ['Borgo Panigale', 'Lame', 'Corticella', 'San Donato', 'Bolognina', 'Santa Viola', 'Barca', 'Saffi', 'Costa Saragozza', 'Colli', 'San Ruffillo', 'Mazzini', 'Murri', 'San Vitale', 'Marconi', 'Irnerio', 'Galvani', 'Malpighi']


def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(x) for x in reader]
    return data


def converter_csv_to_special_json(data):
    listina, lista1, lista2, lista3, lista_finale = [], [], [], [], []
    new_dict, dict_finale = {}, {}
    for elem in lista_zone:
        somma1 = 0
        somma2 = 0
        somma3 = 0
        for row in data:
            if row['Zona'] == elem:
                new_dict.update({'Categoria' : row['Categoria']})
                new_dict.update({'Sottocategoria': row['Sottocategoria']})
                new_dict.update({'Numero Segnalazioni': row['Numero Segnalazioni']})
                listina.append(new_dict)
                new_dict = {}
                if row['Categoria'] == 'Degrado sociale':
                    lista1.append(int(row['Numero Segnalazioni']))
                if row['Categoria'] == 'Degrado ambientale':
                    lista2.append(int(row['Numero Segnalazioni']))
                if row['Categoria'] == 'Microcriminalita':
                    lista3.append(int(row['Numero Segnalazioni']))
        somma1 = sum(lista1)
        somma2 = sum(lista2)
        somma3 = sum(lista3)
        lista1, lista2, lista3 = [],[],[]
        dict_finale.update({'Zona' : elem})
        dict_finale.update({'Totale Degrado Sociale': somma1})
        dict_finale.update({'Totale Degrado Ambientale': somma2})
        dict_finale.update({'Totale Microcriminalita': somma3})
        dict_finale.update({'Segnalazioni': listina})
        listina = []
        dict_finale = {}
        lista_finale.append(dict_finale)

    return (lista_finale)
