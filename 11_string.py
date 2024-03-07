#                             String 

# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
# name = "Harry"
# print("Hello, " + name)

name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
print("Hello, " + name) # output: Hello, Harry

# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
# Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.
# How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience
print('He said, "I want to eat an apple".')

#                         Multiline Strings

#If our string has multiple lines, we can create them like this:
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''
print(apple) 

#                    Accessing Characters of a String............

# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error

#                         Looping through the string..........

# Strings are arrays and arrays are iterable. Thus we can loop through strings.
# We can loop through strings using a for loop like this:
print("Lets use a for loop\n")
for character in apple:
    print(character)
# Above code prints all the characters in the string name one by one!
alphabets = "ABCDE"
for i in alphabets:
    print(i)
# Output:
# A
# B
# C
# D
# E

#                                   String Slicing ......

# Length of a String..............................
# We can find the length of a string using len() function.
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
# Output:
# Mango is a 5 letter word.
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# Output:5

#                         String as an array

# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])
# Note: This method of specifying the start and end index to specify a part of a string is called slicing.
