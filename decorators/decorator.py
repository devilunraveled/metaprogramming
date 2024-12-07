# Simple Decorator with wraps
from functools import wraps

def decorator( tgtFunction ):
	# tgtFunction is the function to be wrapped.
	@wraps(tgtFunction) # NEW LINE ADDED
	def wrapper(*args, **kwargs):
		# Do pre-defined pre-processing
		print(f"Calling {tgtFunction.__qualname__} with {args}, {kwargs}")
		return tgtFunction(*args, **kwargs)
	
	return wrapper
