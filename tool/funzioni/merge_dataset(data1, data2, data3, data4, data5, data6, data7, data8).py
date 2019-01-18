import pandas

lista_zone = ['Borgo Panigale', 'Lame', 'Corticella', 'San Donato', 'Bolognina', 'Santa Viola', 'Barca', 'Saffi', 'Costa Saragozza', 'Colli', 'San Ruffillo', 'Mazzini', 'Murri', 'San Vitale', 'Marconi', 'Irnerio', 'Galvani', 'Malpighi']

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
