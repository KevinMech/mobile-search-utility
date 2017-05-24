import re

FILE_LOCATION = '2016-17-searches.txt'

lines = []
with open(FILE_LOCATION) as file:
    lines = file.readline
