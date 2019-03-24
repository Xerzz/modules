def open_file(file=None):
    if (file == None):  # sprawdzenie nazwy pliku
        print('Nie podano nazwy pliku. Domyslne ustawienie: input.txt')
        file = 'input.txt'
    else:
        print('Wprowadzona nazwa pliku: ' + file)

    try:  # otwarcie pliku, jesli blad to komunikat
        with open(str(file), 'r') as fd:
            file = fd.read().splitlines()
    except IOError:
        print('Blad otwarcia pliku: ' + file)
        exit(1)

    return file
