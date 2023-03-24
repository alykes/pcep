lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        print(lst[r][c])
        if lst[r][c] % 2 != 0: # Trick question because 0 % 2 is 0 as well
            print("#")