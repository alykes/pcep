try:
    raise Exception
except Exception as e:
    print(e.args)
## Result ()


try:
    raise Exception('I don\'t like it')
except Exception as e:
    print(e.args)
## Result ("I don't like it",)

try:
    raise Exception('I don\'t like it', 'in fact, it\'s skata')
except Exception as e:
    print(e.args)
## Result ("I don't like it", "in fact, it's skata")

try:
    1/0
except Exception as e:
    print(e.args)
## Result ('division by zero',)

try:
    5 < 'a'
except Exception as e:
    print(e.args)
## Result ("'<' not supported between instances of 'int' and 'str'",)