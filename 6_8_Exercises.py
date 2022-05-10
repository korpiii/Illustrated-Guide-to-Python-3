#Create a variable, pi, that points to an approximation for the value of π. Create a variable, r, for the radius of a circle that has a value of 10. Calculate the area of the circle (π times the radius squared). You can do multiplication with * and you can square numbers using **. For example, 3**2 is 9.

pi = 3.1416
radius = int(input("What's the radius of the circle?\n"))
area = pi * (radius**2)
print(f"The area is {area}")

#2. Create a variable, b, that points to the base of a rectangle with a value of 10. Create a variable, h, that points to the height of a rectangle with a value of 2. Calculate the perimeter. Change the base to 6 and calculate the perimeter again.

b = 10
h = 2
perimeter = (b * h) * 2
print(f"The perimeter of a rectangle with base {b} and height {h} is {perimeter}\n")

b = 6
perimeter = (b * h) * 2
print(f"The perimeter of a rectangle with base {b} and height {h} is {perimeter}\n")