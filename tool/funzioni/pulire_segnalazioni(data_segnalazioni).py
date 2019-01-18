def pulire_segnalazioni(data_segnalazioni):
    data_segnalazioni[:] = [dict for dict in data_segnalazioni if dict.get('Category') == 'Degrado ambientale' or dict.get('Category') =='Degrado sociale' or dict.get('Category') == 'Microcriminalita']
    return data_segnalazioni
