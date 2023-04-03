class AnimalValueError(ValueError):     # We are using the ValueError class to inherit from.
    pass


def produce_animal_sound(animal_type):
    if animal_type == 'DOG':
        print('woof, woof!')
    elif animal_type == 'CAT':
        print('meow')
    else:
        raise AnimalValueError('That animal type is not available!')


produce_animal_sound('BAT')
## Result: __main__.AnimalValueError: That animal type is not available!