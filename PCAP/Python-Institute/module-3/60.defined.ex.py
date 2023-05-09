# Added some additional tweaks here to have some default values for the constructors,
# which means that when "raising" the exception, you don't need all the parameters
class PizzaError(Exception):
    def __init__(self, pizza = 'unknown', message = 'no such pizza on the menu'):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='unknown', cheese = 101, message = 'too much cheese'):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza)
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese)
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
