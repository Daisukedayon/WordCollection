class StoreToFile_class:
	def fromArrayToFile(cls,Input_List,filename):
		out_f = open(filename,'w')
		out_f.writelines(Input_List)
		out_f.close()
