from goto import goto

@goto
def homosapiens(a):
    #while true:
	for i in [1,2,3]:
		goto .mouse #even while seeing a cat, hearing a word "mouse" makes homosapiens act on a mouse
		if a == "mouse":
			label .mouse
			print("homosapiens does not like mice, ignores them")
			continue
		if a == "dog":
			label .dog
			print("homosapiens likes dogs, throws a bone to them")
			continue
		if a == "cat":
			label .cat
			print("homosapiens likes cats, because they chase and eat mice")
			continue
	return("done")

print(homosapiens("cat"),"finished")
