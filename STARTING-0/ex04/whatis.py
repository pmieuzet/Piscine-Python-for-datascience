import sys

def whatis():
    if len(sys.argv) < 2:
        return
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    
    try:
        value = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if value % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    

try:
    whatis()
except AssertionError as e:
    print("AssertionError: {}".format(e))
