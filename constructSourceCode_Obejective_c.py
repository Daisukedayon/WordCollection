from DataToConstructSourceCode  import DataToConstructSource

class constructSourceCode_Obejective_c:
	def __init__(self):
		self.DataSource = None

	def SetDataToConstructSource(self,obje):
		if not isinstance(obje,SetDataToConstructSource):
			print "Error:object is not data type SetDataToConstructSource\n"
			return 

		self.DataSource = obje

	def ConstructAndOutputArray(self):
		




