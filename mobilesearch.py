import os
import glob


def _pullfiles():
    '''Searches in the folder that the program is currently in and pulls all txt files into a list'''
    folder = os.path.dirname(os.path.realpath(__file__))
    os.chdir(folder)
    files = glob.glob('*.txt')
    return files


def _pulltext(files):
    '''Pull all text from each file pulled'''
    for x in range(0, len(files)):
        with open(files[x]) as file:
            text = file.readlines()
    return text

def init():
    print('Searching files...')
    files = _pullfiles()
    print('Found ' + str(len(files)) + ' files!')
    text = _pulltext(files)


init()
