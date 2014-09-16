from TextHTMLParser import TestHTMLParser
from _curses import ERR

class constructSourceCode_Obejective_c:
	def __init__(self):
		self.DataSource = []

	def SetDataToConstructSource(self,obje):
		self.DataSource = obje
		
	def safe_unicode(obj, * args):
		try:
			return unicode(obj, * args)
		except UnicodeDecodeError:
			ascii_text = str(obj).encode('string_escape')
			return unicode(ascii_text)

	def ConstructAndOutputArray(self,filename):
		import re
		import urllib2
		SourceCode = u""
		Code = u"NSMutableArray *WordStore = [[NSMutableArray alloc] init];\n"
		SourceCode += Code
		
		URL = self.DataSource.pop(0)
		if re.match(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+',URL) == None:
			URL = "//" +URL + "\n"
			SourceCode += URL
			print 'don\'t match URL Regular Expression:' + URL
		
		Code = "NSArray *WordArray1 = @["
		SourceCode += Code
		
		Count = 1
		
		while True:
			if len(self.DataSource) == 0:
				Code = "];\n"
				SourceCode += Code
				break
			URL = self.DataSource.pop(0);
			if  re.match(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+',URL) == None:
				Code = "];\n"
				SourceCode += Code
				Code = "[WordStore addObjectFromArray:WordArray" + str(Count) +"];\n" 
				SourceCode += Code
				Count += 1
				URL = "//"+URL + "\n"
				SourceCode += URL
				
				print 'don\'t match URL Regular Expression:' + URL
				Code = "NSArray WordArray" +str(Count) +"= @["
				SourceCode += Code
			
				
				continue
				
			response = urllib2.urlopen(URL)
			html = response.read()

			parser = TestHTMLParser()
			parser.feed(html)
			for word in parser.returnWordArray():
				try:
					#self.safe_unicode(word)
					if re.match(r'[^\x01-\x7E]',word): 
						print unicode(word,encoding='utf-8')
						#unicode(word,encoding='utf-8')
						SourceCode += '@\"' + unicode(word,encoding='utf-8') + '\",'
				except  UnicodeDecodeError:
					print "Warning:Format is not good"
			SourceCode = SourceCode[:-1] 
		
		Code = "return WordStore;\n"
		SourceCode += Code
		print SourceCode
		out_f = open(filename,'w')
		

		
		#Source = unicode(SourceCode,encoding='utf-8')
		
		
		out_f.write(SourceCode.encode('UTF-8'))
		out_f.close()
				
		




