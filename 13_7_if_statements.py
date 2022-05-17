#1. Write an if statement to determine whether a variable holding a year is a leap year. (See the Numbers chapter exercises for the rules for leap years).

year = int(input("write year \n"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print(f"{year} is leap year")
else:
	print(f"{year} is NOT leap year")

#2. Write an if statement to determine whether a variable holding an integer is odd.

number = int(input("write number\n"))

if number % 2 != 0:
	print(f"{number} is odd")
else:
	print(f"{number} is even")
