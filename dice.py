import random
while True:
	d = input("press r to roll,q to quit.")
	if d == 'r':
		print(random.randint(1,6))
print ("you rolled",random.randint(1,6))
exit(0)