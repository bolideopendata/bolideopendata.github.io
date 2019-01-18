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
