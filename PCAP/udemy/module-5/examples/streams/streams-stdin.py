import sys

for line in sys.stdin:
    if line.rstrip() == 'q':        # need to add rstrip() as every line you enter will add the newline character by default, so won't be able to check just for a 'q'
        break
    print(line)

print('You pressed q, gonna quit!')