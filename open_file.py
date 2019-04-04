def open_file(xfile=None, xmode='r'):
    """
    Available modes:
        'r' - read, default
        'w' - write, WARNING - it overwrites the file if the file exists
        'a' - append
        'r+' - read and write, pointer at the beginning of the file
        'w+' - r and w, WARNING - it overwrites the file if the file exists
        'a+' - r and w, pointer at the end of the file
    Returns file with splitines or None if IOError
    """
    if (xfile == None):  # check file name
        print('File name not provided. Default: input.txt')
        xfile = 'input.txt'
    else:
        print('File name: ' + xfile)

    try:  # open file
        with open(str(xfile), xmode) as fd:
            xfile = fd.read().splitlines()
        return xfile
    except IOError:
        print('Error opening the file: ' + xfile)
        # exit(1)
        return None
