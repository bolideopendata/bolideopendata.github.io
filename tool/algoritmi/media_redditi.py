import pandas

zone_aree = [{'Borgo Panigale': ['Via del Vivaio', 'Lavino di Mezzo', 'Rigosa', 'Casteldebole', 'Triumvirato-Pietra', 'Borgo Centro', 'Ducati-Villaggio Ina', 'Bargellino', 'Aeroporto', 'La Birra', 'Lungo Reno']},
{'Lame': ['Laghetti del Rosario', 'La Noce', 'Tiro A Segno', 'Pescarola', 'Lazzaretto', 'Beverara']},
{'Corticella': ['San Savino', 'Savena Abbandonato', 'Mulino del Gomito', 'Croce Coperta', 'La Dozza']},
{'San Donato': ['Cadriano-Calamosco', 'CAAB', 'Scalo Merci San Donato', 'Pilastro', 'San Donnino', 'Fiera', 'Michelino', 'Via Mondo', 'Via del Lavoro']},
{'Bolognina': ['Caserme Rosse-Manifattura', 'CNR', 'Arcoveggio', 'Via Ferrarese', 'Ex Mercato Ortofrutticolo', 'Piazza dell Unita']},
{'Santa Viola': ['Agucchi', 'Emilia Ponente']},
{'Barca': ['Villaggio della Barca', 'Battindarno', 'Canale di Reno']},
{'Saffi': ['Scalo Ravone', 'Prati di Caprara-Ospedale Maggiore', 'Zanardi', 'Via Vittorio Veneto', 'Velodromo']},
{'Costa Saragozza': ['XXI Aprile', 'Stadio-Meloncello', 'San Giuseppe', 'Ravone', 'Via del Genio', 'San Luca']},
{'Colli': ['Paderno', 'Osservanza', 'San Michele in Bosco']},
{'San Ruffillo': ['Monte Donato', 'Ponte Savena-La Bastia', 'Via Toscana', 'Corelli']},
{'Mazzini': ['Ospedale Bellaria', 'Via Arno', 'Lungo Savena', 'Due Madonne', 'Fossolo', 'Pontevecchio', 'Bitone', 'Cavedone']},
{'Murri': ['Mezzofanti', 'Dagnini', 'Chiesanuova', 'Siepelunga', 'Giardini Margherita']},
{'San Vitale': ['Cirenaica', 'Ospedale Sant Orsola', 'Mengoli', 'Guelfa', 'Scandellara', 'Via Larga', 'Roveri', 'Croce del Biacco', 'Stradelli Guelfi']},
{'Marconi': ['Marconi-1', 'Marconi-2']},
{'Irnerio': ['Irnerio-1', 'Irnerio-2']},
{'Galvani': ['Galvani-1', 'Galvani-2']},
{'Malpighi': ['Malpighi-1', 'Malpighi-2']}]  #Risultato di diz_aree_in_zone(csv_file) in Script delle Segnalazioni

lista_zone = ['Borgo Panigale', 'Lame', 'Corticella', 'San Donato', 'Bolognina', 'Santa Viola', 'Barca', 'Saffi', 'Costa Saragozza', 'Colli', 'San Ruffillo', 'Mazzini', 'Murri', 'San Vitale', 'Marconi', 'Irnerio', 'Galvani', 'Malpighi']

def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        data = [dict(x) for x in reader]
    return data


def reddito_medio_per_zona(data):
    lista_contribuenti, lista_reddito, new_list = [], [], []
    new_dict = {}
    for element in zone_aree:
        for x, y in element.items():
            for z in y:
                for row in data:
                    if z == row['Area statistica']:
                        lista_contribuenti.append(int(row['N contribuenti'].replace('.', '')))
                        lista_reddito.append(int(row['Reddito imponibile ai fini irpef'].replace('.', '')))
            somma = sum(lista_reddito) // sum(lista_contribuenti)
            new_dict.update({'Zona': x})
            new_dict.update({'Reddito medio pro-capite': somma})
            new_list.append(new_dict)
            new_dict = {}
            lista_contribuenti, lista_reddito = [], []
            somma = 0
    return new_list

def merge_dataset(data1, data2, data3, data4, data5, data6, data7, data8):
    new_dict = {}
    new_list, lista_prova = [], []
    for x in lista_zone:
        for row1 in data1:
            if x == row1['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2009' : row1['Reddito medio pro-capite']})
        for row2 in data2:
            if x == row2['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2010' : row2['Reddito medio pro-capite']})
        for row3 in data3:
            if x == row3['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2011' : row3['Reddito medio pro-capite']})
        for row4 in data4:
            if x == row4['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2012' : row4['Reddito medio pro-capite']})
        for row5 in data5:
            if x == row5['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2013' : row5['Reddito medio pro-capite']})
        for row6 in data6:
            if x == row6['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2014' : row6['Reddito medio pro-capite']})
        for row7 in data7:
            if x == row7['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2015' : row7['Reddito medio pro-capite']})
        for row8 in data8:
            if x == row8['Zona']:
                new_dict.update({'Zona' : x})
                new_dict.update({'Reddito medio pro-capite 2016' : row8['Reddito medio pro-capite']})

        new_list.append(new_dict)
        new_dict = {}

        df = pandas.DataFrame(new_list)
        df.to_csv('Redditi_nuova_media_2009-2016.csv', columns=['Zona', 'Reddito medio pro-capite 2009', 'Reddito medio pro-capite 2010', 'Reddito medio pro-capite 2011', 'Reddito medio pro-capite 2012', 'Reddito medio pro-capite 2013', 'Reddito medio pro-capite 2014', 'Reddito medio pro-capite 2015', 'Reddito medio pro-capite 2016'], sep=',', encoding='utf-8',index=False)
    return new_list










