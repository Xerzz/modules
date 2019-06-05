"""
:argument - filename (str)
:returns - absolute path to file in folder of your script
"""
import os


def file_abspath(filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(__location__, filename)
