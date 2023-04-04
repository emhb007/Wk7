import sys
try:
    f = open("foo")
except FileNotFoundError as e:
    print("Could not open", e.filename, e.args[1], file=sys.stderr)
    print("Exception arguments:", e.args, file=sys.stderr)