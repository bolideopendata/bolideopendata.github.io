import pandas


def process_data(source_csv_file_path):
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(x) for x in reader]
    return data

def merge(data1, data2):
    lista_row = []
    for row in data1:
        lista_row.append(row)
    for row in data2:
        lista_row.append(row)
    return lista_row


def sez_elettorali_in_zone_Camera(data):
    lista_zone = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9, lista10, lista11, lista12, lista13, lista14, lista15, lista16, lista17, lista18, lista19 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    new_dict = {}
    new_list = []
    for element in lista_zone:
        for dict in data:
            if element == dict['Zona']:
                #lista1.append(int(dict['Movimento per le Destre unite - Movimento per i Forconi']))
                lista2.append(int(dict['Movimento 5 Stelle']))
                lista3.append(int(dict['Il Popolo della Famiglia']))
                lista4.append(int(dict['Per una Sinistra Rivoluzionaria']))
                lista5.append(int(dict['Partito Comunista']))
                lista6.append(int(dict['Civica Popolare']))
                lista7.append(int(dict['Partito Democratico']))
                lista8.append(int(dict['Italia Europa Insieme']))
                lista9.append(int(dict['Piu Europa']))
                lista10.append(int(dict['Unione di Centro']))
                lista11.append(int(dict['Forza Italia']))
                lista12.append(int(dict['Lega Nord']))
                lista13.append(int(dict['Fratelli d Italia']))
                lista14.append(int(dict['Italia agli Italiani']))
                lista15.append(int(dict['Partito Repubblicano Italiano - Alleanza Liberalpopolare - Autonomie']))
                lista16.append(int(dict['Potere al Popolo']))
                lista17.append(int(dict['Liberi e Uguali']))
                lista18.append(int(dict['CasaPound']))
                lista19.append(int(dict['Totale Voti Validi']))
        new_dict.update({'Zona' : element})
        #new_dict.update({'Movimento per le Destre unite - Movimento per i Forconi': sum(lista1)})
        new_dict.update({'Movimento 5 Stelle': sum(lista2)})
        new_dict.update({'Il Popolo della Famiglia': sum(lista3)})
        new_dict.update({'Per una Sinistra Rivoluzionaria': sum(lista4)})
        new_dict.update({'Partito Comunista': sum(lista5)})
        new_dict.update({'Civica Popolare': sum(lista6)})
        new_dict.update({'Partito Democratico': sum(lista7)})
        new_dict.update({'Italia Europa Insieme': sum(lista8)})
        new_dict.update({'Piu Europa': sum(lista9)})
        new_dict.update({'Unione di Centro': sum(lista10)})
        new_dict.update({'Forza Italia': sum(lista11)})
        new_dict.update({'Lega Nord': sum(lista12)})
        new_dict.update({'Fratelli d Italia': sum(lista13)})
        new_dict.update({'Italia agli Italiani': sum(lista14)})
        new_dict.update({'Partito Repubblicano Italiano - Alleanza Liberalpopolare - Autonomie': sum(lista15)})
        new_dict.update({'Potere al Popolo': sum(lista16)})
        new_dict.update({'Liberi e Uguali': sum(lista17)})
        new_dict.update({'Casa Pound': sum(lista18)})
        new_dict.update({'Totale Voti Validi': sum(lista19)})
        new_list.append(new_dict)
        lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9, lista10, lista11, lista12, lista13, lista14, lista15, lista16, lista17, lista18, lista19 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        new_dict = {}
    return new_list

def percentuale(data):
    new_dict = {}
    lista = []
    lista_partiti = list(data[1])
    print(lista_partiti)
    for dict in data:
        for x, y in dict.items():
            for element in lista_partiti[1:18]:
                new_dict.update({'Zona': dict['Zona']})
                if (x != 'Zona') and (x != 'Totale Voti Validi'):
                    if x == element:
                        tot_voti = int(dict['Totale Voti Validi'])
                        percentuale = round(int(y) * (100 / tot_voti), 2)
                        new_dict.update({x: y})
                        new_dict.update({'Percentuale voti ' + element: str(percentuale)})
                        percentuale = 0
        new_dict.update({'Totale Voti Validi': dict['Totale Voti Validi']})
        lista.append(new_dict)
        new_dict = {}
        df = pandas.DataFrame(lista)
        df.to_csv('Politiche_Camera_Prova.csv', columns=['Zona', 'Movimento 5 Stelle', 'Percentuale voti Movimento 5 Stelle', 'Il Popolo della Famiglia', 'Percentuale voti Il Popolo della Famiglia', 'Per una Sinistra Rivoluzionaria', 'Percentuale voti Per una Sinistra Rivoluzionaria', 'Partito Comunista', 'Percentuale voti Partito Comunista', 'Civica Popolare', 'Percentuale voti Civica Popolare', 'Partito Democratico', 'Percentuale voti Partito Democratico', 'Italia Europa Insieme', 'Percentuale voti Italia Europa Insieme', 'Piu Europa', 'Percentuale voti Piu Europa', 'Unione di Centro', 'Percentuale voti Unione di Centro', 'Forza Italia', 'Percentuale voti Forza Italia', 'Lega Nord', 'Percentuale voti Lega Nord', 'Fratelli d Italia', 'Percentuale voti Fratelli d Italia', 'Italia agli Italiani', 'Percentuale voti Italia agli Italiani', 'Partito Repubblicano Italiano - Alleanza Liberalpopolare - Autonomie', 'Percentuale voti Partito Repubblicano Italiano - Alleanza Liberalpopolare - Autonomie', 'Potere al Popolo', 'Percentuale voti Potere al Popolo', 'Liberi e Uguali', 'Percentuale voti Liberi e Uguali', 'Casa Pound', 'Percentuale voti Casa Pound', 'Totale Voti Validi'], sep=',', encoding='utf-8', index=False)
    return lista

def controllo_percentuale(data):
    listina, lista_prova = [], []
    for dict in data:
        for x,y in dict.items():
            if 'Percentuale' in x:
                listina.append(float(y))
        lista_prova.append(round(sum(listina)))
        listina = []
    return lista_prova
