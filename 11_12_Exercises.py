##Create a string, school, with the name of your elementary school. Examine the methods that are available on that string. Use the help function to view their documentation.

school = "my_school"
##help(str)

##2. Createa string,country,with the value'usa'. Create a new string,correct_country, that has the value in uppercase, by using a string method.

country = "usa"
correct_country = country.upper()
print(correct_country)


##3. Create a string, filename, that has the value 'hello.py'. Check and see if the filename ends with '.java'. Find the index location of 'py'. See if it starts with 'world'.

filename = "hello.py"
print(filename.endswith('.java'))
print(filename.find('py'))
print(filename.startswith("world"))