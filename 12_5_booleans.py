#1. Create a variable, age, set to your age. Create another variable, old, that uses a condition to test whether you are older than 18. The value of old should be True or False.

age = 29
if age > 18:
	old = True
else:
	old =  False
print(old)

#2. Create a variable, name, set to your name. Create another variable, second_half, that tests whether the name would be classified in the second half of the alphabet? What do you need to compare it to?

name = 'korpi'
second_half = name[0] > 'm'
print(second_half)

#3. Create a list, names, with the names of people in a class. Write code to print 'The class is empty!' or 'Class has enrollments.', based on whether there are values in names. (See the tip in this chapter for details).

names = []
if names:
	print("Class has enrollments.")
else:
	print("The class is empty!")

#4. Create a variable, car, set to None. Write code to print 'Taxi for you!', or 'You have a car!', based on whether or not car is set (None is not the name of a car).

car = None
if car:
	print("You have a car!")
else:
	
	print("Taxi for you!")