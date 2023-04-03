try:
    value = int(input('Gimme a number vlaka: '))
    print('The inverse of', value, 'is', 1 / value)
except ValueError:
    print('Oi, that\'s not a number!')
except ZeroDivisionError:
    print('Baaaa, τι λες ρε; 0...?!')
except:
    print('All other exceptions caught here!')
else:
    print('Perfect mang!')      # This is only run if an exception IS NOT raised!
finally:
    print('OK, looks like this block is done...might be a good place to close a connection to a DB ;o)')    # This is run no-matter what!!!
