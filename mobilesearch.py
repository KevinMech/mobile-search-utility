import os
import sys
import glob


def extract():
    ''' Determines whether the second argument is a directory, file, or neither, and extracts the text accordingly.'''
    files = []
    if os.path.isdir(sys.argv[1]):
        directory = os.path.abspath(sys.argv[1])
        os.chdir(directory)
        files = pull_files()
    elif os.path.isfile(sys.argv[1]):
        directory = os.path.dirname(os.path.abspath(sys.argv[1]))
        os.chdir(directory)
        files.append(os.path.basename(sys.argv[1]))
    else:
        error('Please enter a file or directory path as your second argument')
    text = pull_text(files)
    return text


def pull_files():
    '''Searches in the specified directory and pulls all txt files into a list'''
    files = glob.glob('*.txt')
    return files


def pull_text(files):
    '''Extract text from all files specified'''
    text = []
    for i in range(0, len(files)):
        with open(files[i]) as file:
            text += file.readlines()
    return text


def error(message):
    print('error: ' + message)
    print('usage: python3 mobilesearch.py [file/directory]')
    sys.exit(1)


def main():
    extract()


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main()
    else:
        error('Not enough arguments provided!')
