foo = (1, 2, 3)
foo.index(0)
# index tries to find the value in the tuple and return the index
# ValueError

bar = ('one', 'two', 'three')
bar.index('one')    # 0
bar.index('two')    # 1