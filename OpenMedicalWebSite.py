# -*- coding: utf-8 -*-
#医療単語を追加する


import urllib2

#import HTMLParser
from HTMLParser import HTMLParser, HTMLParseError

class TestHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False
    
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
        	print(data)







response = urllib2.urlopen('http://ejje.weblio.jp/category/healthcare/eigky/aa')
html = response.read()

parser = TestHTMLParser()
parser.feed(html)
parser.close()

