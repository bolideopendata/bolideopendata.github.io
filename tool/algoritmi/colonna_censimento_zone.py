import pandas

lista_zone = ['Borgo Panigale', 'Lame', 'Corticella', 'San Donato', 'Bolognina', 'Santa Viola', 'Barca', 'Saffi', 'Costa Saragozza', 'Colli', 'San Ruffillo', 'Mazzini', 'Murri', 'San Vitale', 'Marconi', 'Irnerio', 'Galvani', 'Malpighi']


def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(x) for x in reader]
    return data

def merge_zone_residenti(data):
    lista, new_list = [], []
    new_dict = {}
    for elem in lista_zone:
        for row in data:
            if elem == row['Zona']:
                lista.append(int(row['Residenti']))
        somma = sum(lista)
        lista = []
        new_dict.update({'Zona' : elem})
        new_dict.update({'Residenti' : somma})
        new_list.append(new_dict)
        new_dict = {}
        somma = 0

        df = pandas.DataFrame(new_list)
        df.to_csv('censimento_intermedio.csv', columns=['Zona', 'Residenti'], sep=',', encoding='utf-8', index=False)

    return new_list



