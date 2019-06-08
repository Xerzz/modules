import urllib.request
import os

# example_url = 'https://example.com/text.txt'


def _get_filename_from_url(url: str):
    """
    :param url: str, download file from this url
    :return: tuple
    """
    filename = url.split('/')[-1]
    filename_without_dot = filename.split('.')[0]
    return filename, filename_without_dot


def download(url):
    full_filename, short_filename = _get_filename_from_url(url)
    if full_filename == short_filename:
        full_filename = full_filename + '.html'
    urllib.request.urlretrieve(url, os.getcwd() + '/' + full_filename)


def download_zip(url, extract=True, delete=True):
    import zipfile
    full_filename, short_filename = _get_filename_from_url(url)
    urllib.request.urlretrieve(url, os.getcwd() + '/' + full_filename)

    if extract:
        with zipfile.ZipFile(full_filename, 'r') as zip_file:
            zip_file.extractall(short_filename)

    if delete:
        os.remove(full_filename)
