# Handling an exception inside a function
def bad_fun_in(n):
    try:
        return 1 / n
    except (ZeroDivisionError, ValueError):
        print("Arithmetic Problem!")
    return None

bad_fun_in(0)

print("THE END.")


# Handling an exception outside a function
def bad_fun_out(n):
    return 1 / n

try:
    bad_fun_out(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")