def open_file(xfile='input.txt', xmode='r', xprints=True):
    """
    Parameters:
        xfile (str) - name of file to be opened, default 'input.txt'
        xmode (str) - mode you want to open the file
        xprints (bool) - if True function will print stuff in console

    Returns:
        Array - file with splitines
        or
        None - if IOError

    Available modes:
        'r' - read, default
        'w' - write, WARNING - it overwrites the file if the file exists
        'a' - append
        'r+' - read and write, pointer at the beginning of the file
        'w+' - r and w, WARNING - it overwrites the file if the file exists
        'a+' - r and w, pointer at the end of the file
    """
    if xprints:
        print('File name: ' + xfile)

    try:  # open file
        with open(str(xfile), xmode) as fd:
            xfile = fd.read().splitlines()
        return xfile
    except IOError:
        if xprints:
            print('Error opening the file: ' + xfile)
        # exit(1)
        return None
