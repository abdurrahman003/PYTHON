for i in range(6):
	r = input("press r to roll,q to quit")
	if r =="r":
		if i == 0 or i == 2 or i==3:
			print("you got",6)
		elif i == 4 or i == 1:
			print("you got",2)
		else:
			print("you got",3)
	elif r == "q": 
		print("bye")
		exit()
print("hurray,you won the game") 
