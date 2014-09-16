# -*- coding: utf-8 -*-
#医療単語を追加する


import urllib2

#import HTMLParser
from TextHTMLParser import TestHTMLParser


from MedicalWordURLCollection import MedicalWordURLStore

from StoreToText import StoreToFile_class




URLCollection = MedicalWordURLStore().ReturnURLArray()


response = urllib2.urlopen('http://ejje.weblio.jp/category/healthcare/eigky/aa')
html = response.read()

parser = TestHTMLParser()
parser.feed(html)
StoreToFile_class().fromArrayToFile(parser.returnWordArray(),"MedicalWordText")


parser.close()

