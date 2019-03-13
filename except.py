try:
	a=int(input("enter the number"))
	if a < 5:
		raise TypeError
	elif a==5:
		raise NameError
except NameError:
	print("errorr.....you have chosen number equals to 5")
except TypeError:
	print("errorr...you have chosen number less than 5")
	
else:
	print("no error!!!")
finally:
	print("execution completed")

