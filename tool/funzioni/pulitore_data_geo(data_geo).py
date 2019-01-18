import pandas

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
