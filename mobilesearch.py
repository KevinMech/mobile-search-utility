import os
import sys
import glob
import re


class Search():
    """Object that stores various information about a search result"""

    def __init__(self, persona, searchtype, search):
        self.persona = persona
        self.type = searchtype
        self.search = search


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


def filter(text):
    '''Filter search results, and return list of filtered text'''
    filteredtext = []
    for i in range(0, len(text)):
        # Grab the persona and search type from the string
        split_text = re.split('/', text[i])
        persona = split_text[1]
        search_type = split_text[2]
        # Grabs all text after 'filter=' and before the next & char, and stores in keyword
        keyword = re.search(r'filter=([\w+]+)', text[i])
        # Drops the 'filter=' in keyword string
        filteredkeyword = None
        if keyword is not None:
            filteredkeyword = re.sub(r'filter=', '', keyword.group(0))
        search = Search(persona, search_type, filteredkeyword)
        filteredtext.append(search)
    return filteredtext


def count(filteredtext):
    '''Counts how many times the word appears in the list'''
    keywords = []
    text = []
    results = {}
    # Dump all text we are counting into a list
    for i in range(0, len(filteredtext)):
        text.append(filteredtext[i].search)
    # Dump all unique keyphrases to count into keywords list
    for i in text:
        if i not in keywords:
            keywords.append(i)
    # Count all words in list, and insert results into dictionary
    for i in range(0, len(keywords)):
        count = text.count(keywords[i])
        results[keywords[i]] = count
    return results


def display(results):
    '''Prints results onto screen'''
    for word in sorted(results, key=results.get):
        print(word, results[word])


def error(message):
    '''Print error message to console and exit program'''
    print('error: ' + message)
    print('usage: python3 mobilesearch.py [file/directory]')
    sys.exit(1)


def main():
    text = extract()
    filteredtext = filter(text)
    results = count(filteredtext)
    display(results)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main()
    else:
        error('Not enough arguments provided!')
