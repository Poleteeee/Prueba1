meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso o League of legends",
            'OMG': 'Expresion usada cuando algo es inpresionante o no te lo esperabas',
            'WTF': 'Expresion que se usa cuando no sabes que acaba de pasar tambien traducida como QUE COÑO!',
    
            }

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(word, meme_dict[word])
    else:
        print('Esa palabra no se ha encontrado, revisa si la escribiste bien')
