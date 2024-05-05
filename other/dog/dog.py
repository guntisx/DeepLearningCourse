
def dog(a):
    #while true:
	for i in [1,2,3]:
		if a == "mouse":
			print("dog does not eat mouse, ignores it")
		if a == "dog":
			print("dog likes other dogs, snifs them")
		if a == "cat":
			print("dog hates cats, chases them away")
	return("done")

print(dog("cat"),"finished")
