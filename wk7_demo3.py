import sys

def my_func(*arguments):
    if not all(arguments):
        raise ValueError('False argument in my_func')
try:
    my_func('Tom', '', 42)
except ValueError as err:
    print('Oops:', err, file=sys.stderr)