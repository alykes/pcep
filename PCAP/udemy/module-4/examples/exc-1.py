try:
    value = int(input('Gimme a number vlaka: '))
    print('The inverse of', value, 'is', 1 / value)
except ValueError:
    print('Oi, that\'s not a number!')
except ZeroDivisionError:
    print('Baaaa, τι λες ρε; 0...?!')
except:
    print('All other exceptions caught here!')
