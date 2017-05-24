import re

# Add location for the file to search here
FILE_LOCATION = '2016-17-searches.txt'

# Grab all lines from the file specified
lines = []
with open(FILE_LOCATION) as file:
    lines = file.readlines()

# Iterate through each line in the list
for i in range(0, len(lines)):
    print(lines[i])
