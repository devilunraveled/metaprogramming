from decorator import decorator
import time

def classDecorator(cls):
    # Takes the class as input
    print(f"Runnig the class Decorator at {time.asctime(time.localtime(time.time()))}")
    for attributeName, attribute in vars(cls).items(): # vars gives all the attributes and their names
        if callable(attribute):
            setattr(cls, attributeName, decorator(attribute)) # Set each callable attribute as the decorated attribute
	# ! VERY BAD IDEA TO DO IT THIS WAY
    return cls
