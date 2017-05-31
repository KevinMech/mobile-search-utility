import os
import glob


def _foldersearch():
    '''Searches in the folder that the program is currently in and pulls all txt files into a list'''
    folder = os.path.dirname(os.path.realpath(__file__))
    os.chdir(folder)
    files = glob.glob('*.txt')
    return files


def init():
    print('Searching files...')
    files = _foldersearch()
    print('Found ' + str(len(files)) + ' files!')


init()
