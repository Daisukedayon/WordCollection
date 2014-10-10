# -*- coding: utf-8 -*-
#医療単語を追加する


import urllib2

#import HTMLParser
from TextHTMLParser import TestHTMLParser


from MedicalWordURLCollection import MedicalWordURLStore

from StoreToText import StoreToFile_class

from constructSourceCode_Objective_c_En import constructSourceCode_Objective_c_En




#URLCollection = MedicalWordURLStore().ReturnURLArray()
URLCollection = ['http://ejje.weblio.jp/category/healthcare/eigky/a']

construct = constructSourceCode_Objective_c_En()

construct.SetDataToConstructSource(URLCollection)
construct.ConstructAndOutputArray()