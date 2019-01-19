def calcolo_percentuale(data):
    new_dict = {}
    lista = []
    lista_partiti = list(data[1])
    for dict in data:
        for x, y in dict.items():
            for element in lista_partiti[1:19]:
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
        df.to_csv('Politiche_Senato_intermedio.csv', columns=['Zona', 'Movimento per le Destre unite - Movimento per i Forconi', 'Percentuale voti Movimento per le Destre unite - Movimento per i Forconi', 'Il Popolo della Famiglia', 'Percentuale voti Il Popolo della Famiglia', 'Partito Repubblicato Italiano - Alleanza Liberalpopolare - Autonomie', 'Percentuale voti Partito Repubblicato Italiano - Alleanza Liberalpopolare - Autonomie', 'Potere al Popolo', 'Percentuale voti Potere al Popolo', 'Civica Popolare', 'Percentuale voti Civica Popolare', 'Italia Europa Insieme', 'Percentuale voti Italia Europa Insieme', 'Piu Europa', 'Percentuale voti Piu Europa', 'Partito Democratico', 'Percentuale voti Partito Democratico', 'Per una Sinistra Rivoluzionaria', 'Percentuale voti Per una Sinistra Rivoluzionaria', 'Partito Comunista', 'Percentuale voti Partito Comunista', 'CasaPound', 'Percentuale voti CasaPound', 'Liberi e Uguali', 'Percentuale voti Liberi e Uguali', 'Italia agli Italiani', 'Percentuale voti Italia agli Italiani', 'Movimento 5 Stelle', 'Percentuale voti Movimento 5 Stelle', 'Forza Italia', 'Percentuale voti Forza Italia', 'Unione di Centro', 'Percentuale voti Unione di Centro', 'Lega Nord', 'Percentuale voti Lega Nord', 'Fratelli d Italia', 'Percentuale voti Fratelli d Italia', 'Totale Voti Validi'], sep=',', encoding='utf-8', index=False)

    return lista
