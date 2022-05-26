#1.Create a list with the names of friends and colleagues. Calculate the average length of the names.

friends_names = ['Amelia', 'Emily', 'Michael', 'Madison', 'Isabella', 'Emma', 'Matthew','Lucas', 'Daniel', 'Hannah','Abigail', 'Andrew']
total_length_sum = 0

for name in friends_names:
	total_length_sum = total_length_sum + len(name)

average_length = total_length_sum / len(friends_names)
print(f'Average length of the names is {average_length}\n')

#2. Create a list with the names of friends and colleagues. Search for the name John using a for loop. Print not found if you didn’t find it. (Hint: use else).
if "John" in friends_names:
	print('Found John in list.\n')
else:
	print('John not found\n')


#3. Create a list of tuples of first name,lastname,and age for your friends and colleagues. If you don’t know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age.
friends_full_data =  [('Amelia', 18), ('Emily', 30), ('Michael', 21), ('Madison', 40), ('Isabella', 29), ('Emma', 32), ('Matthew', 35),('Lucas', 54), ('Daniel', None), ('Hannah', 39),('Abigail',25), ('Andrew', 22)]

age_sum = 0
for index, tuple in enumerate(friends_full_data):
	if tuple[1] is None:
		continue
	age_sum = age_sum + tuple[1]

age_average = age_sum / len(friends_full_data)

for index, tuple in enumerate(friends_full_data):
	if tuple[1] is None:
		print(f'{tuple[0]}: age not found')
	elif tuple[1] > age_average:
		print(f'{tuple[0]} is older the average age of {age_average}')
	else:
		print(f'{tuple[0]} is younger the below age of {age_average}')