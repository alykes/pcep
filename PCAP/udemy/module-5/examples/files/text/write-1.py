try:
    stream = open('newfile.txt', 'w')
    stream.write('This is the first line!\n')
    stream.write('This is the second line!\n')
    stream.close()
except Exception as e:
    print('An error occurred:', e)