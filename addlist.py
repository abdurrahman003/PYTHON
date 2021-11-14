def addlist(mylist):
	result=1
	for x in mylist:
		result=result+x
	return result
list1=[1,4,7]
list2=[9,7,5]
print(addlist(list1))
print(addlist(list2))