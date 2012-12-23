#//////////////////////////////////////////////
# wrap to "restrict"
class RestrictingWrapper(object):
	def __init__(self, w, block):
		self._w = w #wrap these methods
		self._block = block #block these methods
	def __getattr__(self, n):
		if n in self._block:
		raise AttributeError, n#this is very important the function sould never retrun None!!!!!
		return getattr(self._w, n)

#//////////////////////////////////////////////
#Abstract/Interface class
class TheInterface(object):
	def doThis(self):
		# provide a default (often a no-op)
		pass
	def doThat(self):
		# or, force subclass to implement
		# (might also just be missing...)
		raise NotImplementedError
#//////////////////////////////////////////////
#DSU Decorate, Sort, Undecorate
decorated = [(entry["date_parsed"], entry) for entry in topentries.values()]
decorated.sort()
decorated.reverse() # for most recent entries first
sorted = [entry for (date,entry) in decorated]
#//////////////////////////////////////////////
#swapping values, without temp values
a, b = b, a
#//////////////////////////////////////////////
#use "in" wherever you can-> implement it in your classes
def __contains__(self,n):
	if n in self.somelist:
		return True

#//////////////////////////////////////////////
#profile your application to check for bugs
python -m cProfile myscript.py>out.profile
