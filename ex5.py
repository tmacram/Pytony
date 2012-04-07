name = 'Tony'
age = 23 # not a lie
height = 70 # inches
weight = 175 #lbs
eyes = 'brown' 
teeth = 'coffee'
hair = 'Brown'
centimeters = height * 2.54
kilograms = weight / 2.2


print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall though" % centimeters
print "He's %d pounds heavy" % weight
print "He's %d heavy in kg's" % kilograms
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d" % (
       age, height, weight, age + height + weight)

#It matters what character you use after the percent sign the letters found here http://docs.python.org/library/stdtypes.html#string-formatting
#are meant to define how to convert the bject or variable you defined string or umber or whatever