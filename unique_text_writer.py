# Write unique lines to a file
import os.path
from os import path
def writeToFile(file, text):
    with open(file, 'a') as newfile:
        newfile.write(text)
        newfile.close()

def dupe_search_set(dir, res):
    lines_seen = set() # holds lines already seen
    add_newline_if_missing_big(dir, 'ISO-8859-1')
    outfile = open(res, "w", encoding = 'ISO-8859-1')
    for line in open(dir, "r", encoding = 'ISO-8859-1'):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

def add_newline_if_missing_big(filename, encoding):
    with open(filename, 'r+', encoding=encoding) as input_file:
        last_line = ""
        count = 0
        for line in input_file:
            count = count + 1
            last_line = line
        print("Line count:",count)
    
    with open(filename, 'r+', encoding=encoding) as new_input_file:
        new_count = 0
        for line in new_input_file:
            new_count = new_count + 1
            if(line == last_line):
                if(line[-1] != '\n' and new_count == count):
                    new_input_file.write("\n")
                    new_input_file.close()
        print("Line count:",new_count)


#if __name__ == '__main__':
#    location = 'name_combination.txt'
#    result = 'test.txt'
#    dupe_search(location, result)