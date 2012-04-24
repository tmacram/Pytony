variable = 0
empty_list = []

while variable < 6:
	print "At the top variable is %d" % variable
	empty_list.append(variable)
	
	variable = variable  + 1
	print "Numbers now: ", empty_list
	print "At the bottom variable is %d" % variable
	
print "Th numbers : "

for num in empty_list:
	print num