#1. Yousleptfor 6.2,7,8,5,6.5,7.1 and 8.5 hours this week.
# Calculatetheaveragenumber of hours slept.

from pickle import TRUE


hours_slept = 6.2 + 7 + 8 + 5 + 6.5 + 7.1 + 8.5
sleeping_avg = hours_slept / 7
print(f"Sleeping average time is {sleeping_avg} hours")


#2. Is 297 divisible by 3?

remainder = 297 % 3
if remainder == 0:
	print("297 is divisible by 3")
else:
	print("297 is not divisible by 3")

#3. What is 2 raised to the tenth power?
result = 2**10
print(f"2 raised to the tenth power is {result} ")
#4. Wikipedia defines leap years as:
#Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.  Write Python code to determine if 1800, 1900, 1903, 2000, and 2002 are leap years.

year_list = [1800, 1900, 1903, 2000, 2002]

for year in year_list:
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		print(f"{year} is leap year")
	else:
		print(f"{year} is NOT leap year")
