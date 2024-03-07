#                               Python Lists

# list tutorial:
# https://www.geeksforgeeks.org/python-lists/

# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.

# Example 1:
# lst1 = [1,2,2,3,5,4,6]
# lst2 = ["Red", "Green", "Blue"]
# print(lst1)
# print(lst2)

# Output:
# [1, 2, 2, 3, 5, 4, 6]
# ['Red', 'Green', 'Blue']

# Example 2:
# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)

# Output:
# ['Abhijeet', 18, 'FYBScIT', 9.8]

#                                    List Index
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

# Example:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]

# Accessing list items
# We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

# Example:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# Output:
# Blue
# Green
# Red

#                   Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# Example:
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# Output:
# Green
# Blue
# Red

# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")

# Output:
# Yellow is present.

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Orange" in colors:
#     print("Orange is present.")
# else:
#     print("Orange is absent.")

# Output:
# Orange is absent.

#                           Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

# Syntax:
# listName[start : end : jumpIndex]

# Note: jump Index is optional. We will see this in later examples.

# Example: printing elements within a particular range:
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

# Output:
# ['mouse', 'pig', 'horse', 'donkey']
# ['bat', 'mouse', 'pig', 'horse', 'donkey']

# Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.
# Note: The element of the end index provided will not be included.

# Example: printing all element from a given index till the end
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[4:])	#using positive indexes
# print(animals[-4:])	#using negative indexes

# Output:
# ['pig', 'horse', 'donkey', 'goat', 'cow']
# ['horse', 'donkey', 'goat', 'cow']

# When no end index is provided, the interpreter prints all the values till the end.

# Example: printing all elements from start to a given index
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[:6])	#using positive indexes
# print(animals[:-3])	#using negative indexes

# Output:
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
# ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']

# When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# Example: Printing alternate values
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[::2])		#using positive indexes
# print(animals[-8:-1:2])	#using negative indexes

# Output:
# ['cat', 'bat', 'pig', 'donkey', 'cow']
# ['dog', 'mouse', 'horse', 'goat']

# Here, we have not provided start and index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

# Example: printing every 3rd consecutive value withing a given range
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[1:8:3])

# Output:
# ['dog', 'pig', 'goat

# Here, jump index is 3. Hence it prints every 3rd element within given index.

#                                      List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter “o” in the new list
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

# Output:
# ['Milo', 'Bruno', 'Rosa']

# Example 2: Accepts items which have more than 4 letters
# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if (len(item) > 4)]
# print(namesWith_O)

# Output:
# ['Sarah', 'Bruno', 'Anastasia']

marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

#                                         List Methods

# list.sort()
# This method sorts the list in ascending order. The original list is updated

# Example 1:
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)
# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)

# Output:
# ['blue', 'green', 'indigo', 'voilet']\
# [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

# Example:
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort(reverse=True)
# print(colors)
# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort(reverse=True)
# print(num)

# Output:
# ['voilet', 'indigo', 'green', 'blue']
# [9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]

# The reverse parameter is set to False by default.
# Note: Do not mistake the reverse parameter with the reverse method.

# reverse()
# This method reverses the order of the list.

# Example:
# colors = ["voilet", "indigo", "blue", "green"]
# colors.reverse()
# print(colors)
# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)

# Output:
# ['green', 'blue', 'indigo', 'voilet']
# [7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]

# index()
# This method returns the index of the first occurrence of the list item.

# Example:
# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.index("green"))
# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(3))

# Output:

# 1
# 3

# count()
# Returns the count of the number of items with the given value.

# Example:
# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))
# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]

# Output:
# 2
# 3

# copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

# Example:
# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# Output:
# ['voilet', 'green', 'indigo', 'blue']
# ['voilet', 'green', 'indigo', 'blue']

# append():
# This method appends items to the end of the existing list.

# Example:
# colors = ["voilet", "indigo", "blue"]
# colors.append("green")
# print(colors)

# Output:
# ['voilet', 'indigo', 'blue', 'green']

# insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# Example:
# colors = ["voilet", "indigo", "blue"]
# #           [0]        [1]      [2]
# colors.insert(1, "green")   #inserts item at index 1
# # updated list: colors = ["voilet", "green", "indigo", "blue"]
# #       indexs              [0]       [1]       [2]      [3]
# print(colors)

# Output:
# ['voilet', 'green', 'indigo', 'blue']

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# Example 1:
# #add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

# Output:
# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# Concatenating two lists:
# You can simply concatenate two lists to join two lists.

# Example:
# colors = ["voilet", "indigo", "blue", "green"]
# colors2 = ["yellow", "orange", "red"]
# print(colors + colors2)

# Output:
# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
# print(k)
# l.extend(m)
print(l)

