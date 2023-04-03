class USerActionException(Exception):           # Inherits directly from Exception
    def __init__(self, message='', user_id=''): # Allows the user to specify arguments
        Exception.__init__(self)                # invoke the constructor of the Super Class
        self.user_id = user_id                  # Invoke two new properties
        self.message = message
    def __str__(self):                          # Override the default __str__ method, so that we can customise what is returned
        return type(self).__name__ + ' occurred. Error message: ' + self.message +', userId: ' + self.user_id


def say_hello(name, user_id):                   # Expects a name and is provided with a user_id
    if name == '':
        raise USerActionException('empty name!', user_id)   # Simply raises a test exception so that we can see how this works if the name is blank!
    print('Yiasou', name)


try:
    say_hello('Adam', 'DT342')
    say_hello('', 'DT342')
except Exception as e:
    print(e)


class EmptyNameUserActionException(USerActionException):
    def __init__(self, user_id=''):
        super().__init__('An empty name was provided!', user_id)

def say_yiasou(name, user_id):
    if name == '':
        raise EmptyNameUserActionException(user_id)
    print('Yiasou,', name, 're vlaka!')

try:
    say_yiasou('Mitso', 'DT342')
    say_yiasou('', 'DT342')
except Exception as e:
    print(e)