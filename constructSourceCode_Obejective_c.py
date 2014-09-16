

class constructSourceCode_Obejective_c:
	def __init__(self):
		self.DataSource = []

	def SetDataToConstructSource(self,obje):
		self.DataSource = obje

	def ConstructAndOutputArray(self):
		SourceCode = []
		Code = "NSMutableArray *WordStore = [[NSMutableArray alloc] init];"
		SourceCode.append(Code)
		
		Code = "NSArray *WordArray1 = @["
		
		while True:
			URL = self.DataSource.pop(0);
			if not URL.match('http(s)?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?'):
				SourceCode.append(URL)
				print 'don\'t match URL:' + URL
				SourceCode.append(Code)
				#ここ、作りかけ
				
				continue
				
			response = urllib2.urlopen(URL)
			html = response.read()

			parser = TestHTMLParser()
			parser.feed(html)
			for word in parser.returnWordArray():
				Code += '@\"' + word + '\",'
			Code = Code[:-1]
			#StoreToFile_class().fromArrayToFile(parser.returnWordArray(),"WordText")
				
		




