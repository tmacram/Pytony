#this is setting a variable x to a string with a string formatting operator
#the string formatting operator is 'd' which is great for decoimal
x = "There are %d types of people." % 10
#this is a variable binary just equal to a string named binary. Simple
binary = "binary"
#This is a variable do not equal to the string don't. Simple
do_not = "don't"
#this is the variable y, that uses 2 string formatting operators (s) meaning it will need a parenthesis
#at the end. s is great for convertng object to strings. in this case our two string variables 
y = "Those who know %s and those who %s" % (binary, do_not)

#The two lines below are just printing the two variable we defined earlier
print x
print y

#Now we are printing a string saying how many types of people there are using 'r' which is a string fomatting operator for strings
print "I said : %r." % x
#Same thing as above. Printing a string so we can have cleaner code and only set the variable to use it over and over. 
print "I also said: '%s'." % y

#this is just a variable used to define hilarity
hilarious = False
#this is the jo eval variable used in the next mathematical expression 
joke_evaluation = "Isn't that joke so funny?! %r"

#So now we're printing the string from joke evaluation and still using the formatting operator % for false in the hilarious variable
print joke_evaluation % hilarious
#definign 2 variables 
w = "This is the left side of..."
e = "a string with a right side."
#Printing 2 variables to demonstrate a point. 
print w + e
