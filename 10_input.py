#              Input functions

#In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable
#    variable=input()
v = input("Enter your name: ")
print("My name is", v)
# output: 
# Enter your name: (input your name)
# My name is (print the input syntax)

# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.
#variable=int(input())
# variable=float(input())
p = input("Enter first number: ")
q = input("Enter second number: ")
print(p  + q)

print(int(p) + int(q))