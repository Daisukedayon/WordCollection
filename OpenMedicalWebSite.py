# -*- coding: utf-8 -*-
#医療単語を追加する


import urllib2

#import HTMLParser
from TextHTMLParser import TestHTMLParser


from MedicalWordURLCollection import MedicalWordURLStore

from StoreToText import StoreToFile_class




URLCollection = MedicalWordURLStore().ReturnURLArray()


for url in URLCollection:
    if not url.match(
        print url +"don't matches URL"
        
    response = url
    html = response.read()
    parser = TestHTMLParser()
    parser.feed(html)
    StoreToFile_class().fromArrayToFile(parser.returnWordArray(),"MedicalWordText")


parser.close()
    


response = urllib2.urlopen('http://ejje.weblio.jp/category/healthcare/eigky/aa')
html = response.read()

parser = TestHTMLParser()
parser.feed(html)
StoreToFile_class().fromArrayToFile(parser.returnWordArray(),"MedicalWordText")


parser.close()

