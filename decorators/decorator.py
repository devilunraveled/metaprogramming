# Simple Decorator with wraps
from functools import wraps
import time

def decorator( tgtFunction ):
    # tgtFunction is the function to be wrapped.
    print(f"Decorated {tgtFunction.__qualname__} at {time.asctime(time.localtime(time.time()))}")
    @wraps(tgtFunction) # NEW LINE ADDED
    def wrapper(*args, **kwargs):
        # Do pre-defined pre-processing
        print(f"Calling {tgtFunction.__qualname__} with {args}, {kwargs} at {time.asctime(time.localtime(time.time()))}")
        return tgtFunction(*args, **kwargs)

    return wrapper

# Decorator with arguments
def generalDecorator( printInputs : bool ):
    def decorator( tgtFunction ):
        # tgtFunction is the function to be wrapped.
        @wraps(tgtFunction)
        def wrapper(*args, **kwargs):
            # Do pre-defined pre-processing
            if printInputs :
                print(f"Calling {tgtFunction.__qualname__} with {args}, {kwargs}")
            else :
                print(f"Calling {tgtFunction.__qualname__}")
            return tgtFunction(*args, **kwargs)

        return wrapper # Returns the actual function wrapper .
    return decorator # Returns the customized decorator .

def getNameDecorator(tgtFunction):
    print("Decorating with the getNameDecorator")
    @wraps(tgtFunction)
    def wrapper(*args, **kwargs):
        # Do pre-defined pre-processing]
        print(f"Accessing the name of the student at {time.asctime(time.localtime(time.time()))}")
        return tgtFunction(*args, **kwargs)
    return wrapper
