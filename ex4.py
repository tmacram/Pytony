cars = 100
#the above line sets the variable "cars" equal to 100
space_in_a_car= 4.0 
#spca in the car variable set equal to 4
drivers = 30
#setting the drivers variable equal to 30
passengers = 90 
# setting the passaengers variable equal to ninety
cars_not_driven = cars - drivers
#this variables usue the 2 previosuly defined variable to come to a conclusion about how many cars we can take. 
cars_driven = drivers 
#this variable is defining a variables cars driven to denote how many 
carpool_capacity = cars_driven * space_in_a_car
#this variable is meant to define how many people can fit in this carpooling trip on average
average_passengers_per_car = passengers / cars_driven

#this grabs the cars variable and explains how many cars there are
print "There are ", cars, "cars available."
#this grabs the rivers variable, previously defined, and explains how many drover there are to drive
print "There are only", drivers, "drivers available"
#this grabs the cars not driven variable to explain how many empt cars there will be
print "There will be", cars_not_driven, " empty cars today."
#this explins how much room we hav among the cars
print "We can transport", carpool_capacity, "people today."
#this explains how many people we need to transport
print "We have", passengers, "to carpool today."
#this explains on average how many people we need to put in cars.
print "We need to put about", average_passengers_per_car, "in each car."

#his carpool capacity comment carpool was one word