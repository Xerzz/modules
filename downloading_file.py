import urllib.request
import os


# example_url = 'https://example.com/text.txt'


def _get_filename_from_url(url: str):
    """
    Args:
        url: str, download file from this url
    Returns:
        tuple with full name (with file extension) and short name (without it)
    """
    filename = url.split('/')[-1]
    filename_without_dot = filename.split('.')[0]
    return filename, filename_without_dot


def download(url):
    full_filename, short_filename = _get_filename_from_url(url)
    if full_filename == short_filename:
        full_filename = full_filename + '.html'
    print('Downloading file ' + full_filename + '...')
    urllib.request.urlretrieve(url, os.getcwd() + '/' + full_filename)
    print('Done!')
    return full_filename, short_filename


def download_zip(url, extract=True, delete=True):
    import zipfile
    full_filename, short_filename = download(url)
    # file downloaded, trying to extract
    try:
        if extract:
            with zipfile.ZipFile(full_filename, 'r') as zip_file:
                print('Extracting...')
                zip_file.extractall(short_filename)
                print('Done!')
        if extract and delete:
            os.remove(full_filename)
            print('File deleted, only folder left')
    except zipfile.BadZipFile as error:
        print('WARNING! ' + str(error))
