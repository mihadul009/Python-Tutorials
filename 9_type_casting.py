#                          type-casting 

#The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

z = "1"
m = "2"
print(z+m) #output: 12

w = "Mihadul"
t = "Islam"
print(w+t) # output: MihadulIslam

# basic type-casting
s = "1" # string
# s = 1
k = "2" # string
# k = 2
print(int(s) + int(k)) # output: 3

#    Two Types of Typecasting:

#            Explicit Conversion (programer command python to convert this data-type into this data-type)
# The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.
# It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
# output: The Sum of both the numbers is 22


#         Implicit Conversion (Implicit type casting in python)
#Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.
#Python converts a smaller data type to a higher data type to prevent data loss.
# Python automatically converts
# n to int
n = 7
print(type(n))
 
# Python automatically converts o to float
o = 3.0
print(type(o))
 
# Python automatically converts j to float as it is a float addition
j = n + o
print(j)
print(type(j))

# output:
# <class 'int'>
# <class 'float'>
# 10.0
# <class 'float'>