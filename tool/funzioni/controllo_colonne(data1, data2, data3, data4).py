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
