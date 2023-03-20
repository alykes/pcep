d = {}
d['2'] = [1, 2] # '2' does not not signify an order
d['1'] = [3, 4] # '1' does not not signify an order

for x in d.keys():
    print(d[x][1], end="")
