from TextHTMLParser import TestHTMLParser
from _curses import ERR

class constructSourceCode_Objective_c_En:
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

    def ConstructAndOutputArray(self):
        import re
        import urllib2
        SourceCode = u""
        #Code = u"NSMutableArray *WordStore = [[NSMutableArray alloc] init];\n"
        #SourceCode += Code
        
        URL = self.DataSource[0]
        if re.match(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+',URL) == None:
            URL = "//" +URL + "\n"
            SourceCode += URL
            print 'don\'t match URL Regular Expression:' + URL
            self.DataSource.pop(0)
            
        Code = self.DataSource[0]
        SourceCode += "//"+Code + "\n" 
        
        Code = "WordArray = @["
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
                Code = "[WordStore addObjectFromArray:WordArray];\n" 
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
                    if re.match('/^[a-zA-Z\s]+$/',word): 
                        print unicode(word,encoding='utf-8')
                        #unicode(word,encoding='utf-8')
                        SourceCode += '@\"' + unicode(word,encoding='utf-8') + '\",'
                except  UnicodeDecodeError:
                    print "Warning:Format is not good"
            SourceCode = SourceCode[:-1] 
        
        Code = "[WordStore addObjectsFromArray:WordArray];\n"
        SourceCode += Code
        print SourceCode