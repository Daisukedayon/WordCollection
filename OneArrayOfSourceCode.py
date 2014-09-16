class OneArrayOfSourceCode:
	def __init__(self):
		self.ArrayOfURL = []
		self.Description = ""

	def setDescription(self,desc):
		self.Description = desc

	def addURL(self,url):
		if not isinstance(url,basestring):
			print "Error: object is not string"
			return
		self.ArrayOfURL.append(url)

	def addURLArray(self,ary):
		if not isinstance(ary,list):
			print "Error: object is not list"
		self.extends(array)