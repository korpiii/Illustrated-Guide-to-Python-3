#1. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list. What is the first item in the list? What is the second item in the list?
names = list()
print(names)
print(f'names id is {id(names)}')
names.append('juana')
print(names)
print(f'names id is {id(names)}')
names.append('maria')
print(names)
print(f'names id is {id(names)}')
print(f'the first item in list is names[0] {names[0]}\n the second item is names[1] {names[1]}')

#2. Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it. Make more tuples with the corresponding information from your friends and append them to the list. Sort the list. When you learn about functions, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.
me = ('d_first_name', 'd_last_name', 29)
people = list()
people.append(me)
friend_1 = ('k_first_name', 'c_last_name', 31)
friend_2 = ('d_first_name', 'c_last_name', 25)
people.append(friend_1)
people.append(friend_2)
print(people)
people.sort(key=str)
print(people)
#3. Create a list of the names of the first names your friends. Create a list with the top ten common names. Use set operations to see if any of your friends have common names.
friends_names = ['Amelia', 'Emily', 'Michael', 'Madison', 'Isabella', 'Emma', 'Matthew','Lucas', 'Daniel', 'Hannah','Abigail', 'Andrew']
top_common_names = ['Liam','Olivia','Noah','Emma','Oliver','Charlotte','Elijah','Amelia','James','Ava','William','Sophia','Benjamin','Isabella','Lucas','Mia','Henry','Evelyn','Theodore','Harper']
friends_name_set = set(friends_names)
top_common_names_set = set(top_common_names)
friend_common_name_set = friends_name_set & top_common_names_set
print(f"these folks' names are common {friend_common_name_set}")

#4. Go to Project Gutenberg11 and find a page of text from Shakespeare. Paste it into a triple-quoted string. Create another string with a paragraph of text from Ralph Waldo Emerson. Use the string’s .split method to get a list of words from each. Using set operations find the common words and words unique to both authors.

#5. Tuples and lists are similar but have different behavior. Use set operations to find the attributes of a list object that are not in a tuple object.