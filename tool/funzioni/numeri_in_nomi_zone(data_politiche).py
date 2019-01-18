lista_zone = [{'3' : 'Borgo Panigale'}, {'1' : 'Barca'}, {'6' : 'Costa Saragozza'}, {'4' : 'Colli'}, {'16' : 'San Ruffillo'}, {'9' : 'Lame'}, {'17' : 'Santa Viola'}, {'14' : 'Saffi'}, {'2' : 'Bolognina'}, {'5' : 'Corticella'}, {'15' : 'San Donato'}, {'18' : 'San Vitale'}, {'12' : 'Mazzini'}, {'13' : 'Murri'}, {'8' : 'Irnerio'}, {'7' : 'Galvani'}, {'10' : 'Malpighi'}, {'11' : 'Marconi'}]

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
