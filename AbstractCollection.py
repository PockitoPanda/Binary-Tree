class AbstractCollection:

	def __init__(self, source_collection=None):
		""" Sets the initial state of self, which includes the contents of source_collection """

		self._numitems = 0
		if source_collection:
			for item in source_collection:
				self.add(item)

	def __len__(self):
		""" Return the number of items in this collection """
		return self._numitems

	def is_empty(self):
		""" Returns True if the collection is empty and False otherwise """
		return len(self) == 0

	def __add__(self, other):
		""" Overloads the + operator. A new collection is created with everything from self and other. """
		result = type(self)(self)
		for item in other:
			result.add(item)
		return result

	def count(self, item):
		result = 0
		for i in self:
			if i == item:
				result += 1
		return result