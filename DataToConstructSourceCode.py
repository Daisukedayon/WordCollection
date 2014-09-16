from OneArrayOfSourceCode import OneArrayOfSourceCode


class DataToConstructSource:
	def __init__(self):
		self.ArrayOf_OneArraySourceCode = []
		self.ConstructSpecifiedLanguageSourceCode = None

	def add_OneArrayOfSourceCode(self.onearray):
		if not isinstance(onearray,OneArrayOfSourceCode):
			print "Error:Object is not OneArrayOfSourceCode\n"
			return 

		self.ArrayOf_OneArraySourceCode.append(onearray)

	def return_ArrayOf_OneArraySourceCode(self):
		return self.ArrayOf_OneArraySourceCode

	def setConstructSpecifiedLanguageSourceCode(self,specifiedlanguage):
		self.ConstructSpecifiedLanguageSourceCode = specifiedlanguage
