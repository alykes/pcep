# This program will open a file and count the characters in it (including \n)
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)          # increment by 1 character
    while ch != '':
        print(ch, end='')
        cnt += 1            # update the counter
        ch = s.read(1)      # increment by 1 character
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


from os import strerror
