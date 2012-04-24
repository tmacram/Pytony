print " You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cale. What do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear"
	
	bear = raw_input("> ")

	if bear == "1":
		print "Your face has been ripped off, goodnight."
	elif bear == "2":
		print "Your legs have been devoured in no time at all!"
	else: 
		print "Wise choice you dont take shit from anyone"

elif door == "2":
	print " You stare into the endless ayss at Cthulhu's retina."
	print "1. Blueberries"
	print "2. Some weird ass programming joke."
	print "3. Some thing having to do with sleep/wearable tech."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello."
	else:
		print " I dont know but this is a weird one!"
else:
	print " you stumble around and fall on a knife and die. Great work mayne!"