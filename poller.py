
def poller():
	global ques
	global options

	pollstr = "?poll"  + ';' +ques 

	for answers in options:
		pollstr += ';' + answers

	return pollstr

listofpolls = []

run2 = True
while run2:
	ques = str(input("Enter the question: "))
	if ques == "":
		run2 = False
		run = False
	options = []

	run = True
	num = 1

	while run:
		inp = str(input("Enter option " +str(num)+ " : "))
		if inp == "":
			run = False
		options.append(inp)
		num += 1
	if ques != "":	
		listofpolls.append(poller())
	print()	
	print("SAVED!!")
	print(poller())
	print()

for x in range(len(listofpolls)):
	print(listofpolls[x])

