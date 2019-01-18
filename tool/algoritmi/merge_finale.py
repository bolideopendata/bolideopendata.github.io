import pandas

lista_zone = [{'3' : 'Borgo Panigale'}, {'1' : 'Barca'}, {'6' : 'Costa Saragozza'}, {'4' : 'Colli'}, {'16' : 'San Ruffillo'}, {'9' : 'Lame'}, {'17' : 'Santa Viola'}, {'14' : 'Saffi'}, {'2' : 'Bolognina'}, {'5' : 'Corticella'}, {'15' : 'San Donato'}, {'18' : 'San Vitale'}, {'12' : 'Mazzini'}, {'13' : 'Murri'}, {'8' : 'Irnerio'}, {'7' : 'Galvani'}, {'10' : 'Malpighi'}, {'11' : 'Marconi'}]

def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(x) for x in reader]
    return data

def numeri_in_nomi_zone(data_politiche):
    new_dict = {}
    lista = []
    for diz in lista_zone:
        for x,y in diz.items():
            for row in data_politiche:
                if x == row['Zona']:
                    new_dict.update({'Zona': y})
                    for key, value in row.items():
                        if key != 'Zona':
                            new_dict.update({key : value})
        lista.append(new_dict)
        new_dict = {}
    return lista

def merge_finale(data1, data2, data3, data4):
    new_list = []
    new_dict = {}
    for x1 in data1:
        for x2 in data2:
            for x3 in data3:
                for x4 in data4:
                    if x1['Zona'] == x2['Zona'] == x3['Zona'] == x4['Zona']:
                        new_dict.update({'Zona': x1['Zona']})
                        for elem, value in x1.items():
                            if elem != 'Zona':
                                new_dict.update({elem:value})
                        for elem2, value2 in x2.items():
                            if elem2 != 'Zona':
                                new_dict.update({elem2 + ' Camera':value2})
                        for elem3, value3 in x3.items():
                            if elem3 != 'Zona':
                                new_dict.update({elem3 + ' Senato':value3})
                        for elem4, value4 in x4.items():
                            if elem4 != 'Zona':
                                new_dict.update({elem4:value4})

        new_list.append(new_dict)
        new_dict = {}

    df = pandas.DataFrame(new_list)
    df.to_csv('merge_finale_3csv.csv', columns=['Zona', 'Reddito medio pro-capite 2009', 'Reddito medio pro-capite 2010', 'Reddito medio pro-capite 2011', 'Reddito medio pro-capite 2012', 'Reddito medio pro-capite 2013', 'Reddito medio pro-capite 2014', 'Reddito medio pro-capite 2015', 'Reddito medio pro-capite 2016', 'Movimento 5 Stelle Camera', 'Percentuale voti Movimento 5 Stelle Camera', 'Il Popolo della Famiglia Camera', 'Percentuale voti Il Popolo della Famiglia Camera', 'Per una Sinistra Rivoluzionaria Camera', 'Percentuale voti Per una Sinistra Rivoluzionaria Camera', 'Partito Comunista Camera', 'Percentuale voti Partito Comunista Camera', 'Civica Popolare Camera', 'Percentuale voti Civica Popolare Camera', 'Partito Democratico Camera', 'Percentuale voti Partito Democratico Camera', 'Italia Europa Insieme Camera', 'Percentuale voti Italia Europa Insieme Camera', 'Piu Europa Camera', 'Percentuale voti Piu Europa Camera', 'Unione di Centro Camera', 'Percentuale voti Unione di Centro Camera', 'Forza Italia Camera', 'Percentuale voti Forza Italia Camera', 'Lega Nord Camera', 'Percentuale voti Lega Nord Camera', 'Fratelli d Italia Camera', 'Percentuale voti Fratelli d Italia Camera', 'Italia agli Italiani Camera', 'Percentuale voti Italia agli Italiani Camera', 'Partito Repubblicano Italiano - Alleanza Liberalpopolare - Autonomie Camera', 'Percentuale voti Partito Repubblicano Italiano - Alleanza Liberalpopolare - Autonomie Camera', 'Potere al Popolo Camera', 'Percentuale voti Potere al Popolo Camera', 'Liberi e Uguali Camera', 'Percentuale voti Liberi e Uguali Camera', 'Casa Pound Camera', 'Percentuale voti Casa Pound Camera', 'Totale Voti Validi Camera', 'Movimento per le Destre unite - Movimento per i Forconi Senato', 'Percentuale voti Movimento per le Destre unite - Movimento per i Forconi Senato', 'Il Popolo della Famiglia Senato', 'Percentuale voti Il Popolo della Famiglia Senato', 'Partito Repubblicato Italiano - Alleanza Liberalpopolare - Autonomie Senato', 'Percentuale voti Partito Repubblicato Italiano - Alleanza Liberalpopolare - Autonomie Senato', 'Potere al Popolo Senato', 'Percentuale voti Potere al Popolo Senato', 'Civica Popolare Senato', 'Percentuale voti Civica Popolare Senato', 'Italia Europa Insieme Senato', 'Percentuale voti Italia Europa Insieme Senato', 'Piu Europa Senato', 'Percentuale voti Piu Europa Senato', 'Partito Democratico Senato', 'Percentuale voti Partito Democratico Senato', 'Per una Sinistra Rivoluzionaria Senato', 'Percentuale voti Per una Sinistra Rivoluzionaria Senato', 'Partito Comunista Senato', 'Percentuale voti Partito Comunista Senato', 'CasaPound Senato', 'Percentuale voti CasaPound Senato', 'Liberi e Uguali Senato', 'Percentuale voti Liberi e Uguali Senato', 'Italia agli Italiani Senato', 'Percentuale voti Italia agli Italiani Senato', 'Movimento 5 Stelle Senato', 'Percentuale voti Movimento 5 Stelle Senato', 'Forza Italia Senato', 'Percentuale voti Forza Italia Senato', 'Unione di Centro Senato', 'Percentuale voti Unione di Centro Senato', 'Lega Nord Senato', 'Percentuale voti Lega Nord Senato', 'Fratelli d Italia Senato', 'Percentuale voti Fratelli d Italia Senato', 'Totale Voti Validi Senato', 'Residenti'], sep=',', encoding='utf-8', index=False)
    return new_list

def controllo_row(data1, data2, data3):
    print (len(data1))
    print (len(data2))
    print (len(data3))

def controllo_colonne(data1, data2, data3, data4):
    len_redditi = len(data1[0])
    len_camera = len(data2[0])
    len_senato = len(data3[0])
    len_residenti = len(data4[0])
    if len_camera - 1 + len_redditi + len_senato - 1 + len_residenti - 1 == 82:
        print ('BRAVI!')
    print (len_redditi)
    print(len_camera)
    print(len_senato)
    print(len_residenti)

