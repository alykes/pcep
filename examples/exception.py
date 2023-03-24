try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print('Value Error')
except ZeroDivisionError:
    print('Zero Division Error')
except TypeError:
    print('Type Error')
except:
    print('All other exceptions')


try:
    print(5/0)
    #break       # Another trick question, this does not belong in a try block
except:
    print("sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print('Either Value or Zero Division Error')