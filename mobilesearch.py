import os
import glob


def _pull_files():
    '''Searches in the folder that the program is currently in and pulls all txt files into a list'''
    folder = os.path.dirname(os.path.realpath(__file__))
    os.chdir(folder)
    files = glob.glob('*.txt')
    return files


def _pull_text(files):
    '''Pull all text from each file pulled'''
    for x in range(0, len(files)):
        with open(files[x]) as file:
            text = file.readlines()
    return text


def main():
    print('Searching files...')
    files = _pull_files()
    print('Found ' + str(len(files)) + ' files!')
    text = _pull_text(files)


if __name__ == '__main__':
    main()
