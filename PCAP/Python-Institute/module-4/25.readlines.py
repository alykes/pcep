# This program will read the contents of a file using the readlines() method.
# Note that the method can take a single argument (buffer size in characters or bytes)
#   - If the buffer (argument) you specify is smaller than the line, it will read the entire line.  
#   - If the buffer (argument) you specify is larger than the line but smaller than the next line, it will only read the first line.  
#   - If the buffer (argument) you specify is larger than the line and larger than the next line, it will combine both lines into a single element.  
# NOTE if you just use readlines() without any argument, it will read the entire file and attempt to put each line into an element of a single list, no loop required!
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

