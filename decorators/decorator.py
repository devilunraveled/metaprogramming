# Simple Decorator
def decorator( tgtFunction ):
	# tgtFunction is the function to be wrapped.
	def wrapper(*args, **kwargs):
		# Do pre-defined pre-processing
		print(f"Calling {tgtFunction.__name__} with {args}, {kwargs}")
		return tgtFunction(*args, **kwargs)
	
	return wrapper
