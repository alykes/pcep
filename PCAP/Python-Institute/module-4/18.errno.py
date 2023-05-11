# This is an example of how to access an error in the stream.
try:
    pass                # Some stream operations.
except IOError as exc:
    print(exc.errno)    # The errno is a predefined symbolic constant defined in the "errno" module

