the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list

for twat in the_count:
	print "This is count %d" % twat
# same as above

for fruity in fruits:
	print "This is fruits %s" % fruity
	
	
#also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it!!!

for i in change:
	print "This is our change %r" % i
	
	
# we can also build list, first start with an empty one

empty = range(0,6)

# then use the range function to do 0 to 5 counts

# for i in range(1,6):
# 	print "adding %d to the empty list." % i
# 	#sppend is a function that lists understand
# 	empty.append(i)
# 	
# # now we can print them out too
# 
for i in empty:
	print "Empty was: %d" % i