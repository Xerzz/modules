"""
Simple module that help us opening file
"""

def open_file(xfile: str = 'input.txt',
              xmode: str = 'r',
              xprints: bool = True):
    """
    Parameters:
        xfile (str) - name of file to be opened, default 'input.txt'
        xmode (str) - mode you want to open the file
        xprints (bool) - if True function will print stuff in console

    Returns:
        list - file with splitines

    Raises:
        IOError - when there is no file or when there is another problem with file (permissions etc...)

    Available modes:
        'r' - read, default
        'w' - write, WARNING - it overwrites the file if the file exists
        'a' - append
        'r+' - read and write, pointer at the beginning of the file
        'w+' - r and w, WARNING - it overwrites the file if the file exists
        'a+' - r and w, pointer at the end of the file
    """

    if xmode not in ['r', 'r+', 'w', 'w+', 'a', 'a+']:
        if xprints:
            print('WARNING: Wrong mode chosed, setting default - r')
        xmode = 'r'

    if xprints:
        print('File name: ' + xfile)

    # open file
    try:
        with open(str(xfile), xmode) as fd:
            xfile = fd.read().splitlines()
        return xfile
    except IOError:
        # if xprints:
            # print('Error opening the file: ' + xfile)
        # return None
        raise IOError('Error opening the file' + xfile)
