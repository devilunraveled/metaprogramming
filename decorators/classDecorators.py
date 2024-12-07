from decorator import decorator

def classDecorator(cls):
	# Takes the class as input
	for attributeName, attribute in vars(cls).items(): # vars gives all the attributes and their names 
		if callable(attribute):
			setattr(cls, attributeName, decorator(attribute)) # Set each callable attribute as the decorated attribute
	# ! VERY BAD IDEA TO DO IT THIS WAY
