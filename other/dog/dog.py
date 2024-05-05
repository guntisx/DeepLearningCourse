
def dog(a):
    #while true:
	for i in [1,2,3]:
		if a == "mouse":
			print("dog does not eat mouse, ignores it")
			continue
		if a == "dog":
			print("dog likes other dogs, snifs them")
			continue
		if a == "cat":
			print("dog hates cats, chases them away")
			continue
		if a == "cat":
			print("dog hates cats, chases them away")
			continue	
	return("done")

print(dog("cat"),"finished")
