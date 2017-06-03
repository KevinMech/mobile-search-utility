import os
import sys
import glob


def pull_files(folder):
    '''Searches in the folder that the program is currently in and pulls all txt files into a list'''
    os.chdir(folder)
    files = glob.glob('*.txt')
    return files


def pull_text(files, single):
    '''Extract text from all files specified'''
    if single:
        with open(files) as file:
            text = file.readlines()
    else:
        for i in range(0, len(files)):
            with open(files[i]) as file:
                text = file.readlines()
    print(text)
    return text


def main():
    # Check to see whether the first argument is a directory or file.
    if os.path.isdir(sys.argv[1]):
        # print('is directory')
        files = pull_files(sys.argv[1])
        pull_text(files, False)
    elif os.path.isfile(sys.argv[1]):
        # print('is file')
        file = os.path.basename(sys.argv[1])
        pull_text(file, True)
    else:
        print('Error: Please specifiy either a file or directory in your first argument')


if __name__ == '__main__':
    main()
