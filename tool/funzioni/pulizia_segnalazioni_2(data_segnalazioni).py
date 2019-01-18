import pandas

def pulizia_segnalazioni_2(data_segnalazioni):
    new_dict = {}
    new_list = []
    for row in data_segnalazioni:
        new_dict.update({'Zona' : row['Zona']})
        if row['Categoria'] == 'Degrado ambientale':
            new_dict.update({'Categoria Segnalazione' : 'Ambientale'})
        if row['Categoria'] == 'Degrado sociale':
            new_dict.update({'Categoria Segnalazione': 'Sociale'})
        if row['Categoria'] == 'Microcriminalita':
            new_dict.update({'Categoria Segnalazione': 'Microcriminalita'})
        new_dict.update({'Sottocategoria Segnalazione': row['Sottocategoria']})
        new_dict.update({'Numero Segnalazioni': row['Numero Segnalazioni']})
        new_list.append(new_dict)
        new_dict = {}

        df = pandas.DataFrame(new_list)
        df.to_csv('Segnalazioni_2017_2.csv', columns=['Zona', 'Categoria Segnalazione', 'Sottocategoria Segnalazione', 'Numero Segnalazioni'], sep=',', encoding='utf-8', index=False)

    return new_list
