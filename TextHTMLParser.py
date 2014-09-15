from HTMLParser import HTMLParser, HTMLParseError


class TestHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False
        self.WordArray = []
    
    def handle_starttag(self, tag, attrs):
    	if tag.lower() == "a":
    		attrs = dict(attrs)
    		class_val = "crosslink"
    		if "class" in attrs:
    			if class_val == attrs["class"]:
      				self.is_a = True


    def handle_endtag(self, tag):
    	if tag.lower() == "a":
    		self.is_a = False

    def handle_data(self, data):
    	if self.is_a is True:
            self.WordArray.append(data)
        	#print(data)

    def returnWordArray():
        return self.returnWordArray