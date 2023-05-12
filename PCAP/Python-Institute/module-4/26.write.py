# This writes one character at a time to a file.
from os import strerror

try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)           # you can also just fo.write(s) which wouldn't require the for loop above
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

# This is added code to read the contents back and count the characters
print('-----------------------------')
print('Now reading back the contents')
print('-----------------------------')

try:
    stream = open('newtext.txt', 'r')

    ccnt = 0
    line = stream.readline()
    
    while len(line) != 0:
        for char in line:
            ccnt += 1
            print(char, end='')  
        line = stream.readline()
    
    print('There are :', ccnt, "characters")
    
    stream.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))  
