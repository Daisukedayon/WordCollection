# -*- coding: utf-8 -*-
#医療単語を追加する


import urllib2

#import HTMLParser



from MedicalWordURLCollection import MedicalWordURLStore




URLCollection = ['http://ejje.weblio.jp/category/healthcare/eigky/aa']



response = urllib2.urlopen('http://ejje.weblio.jp/category/healthcare/eigky/aa')
html = response.read()

parser = TestHTMLParser()
parser.feed(html)
parser.close()

