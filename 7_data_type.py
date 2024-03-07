#                         Data-type

# x = "Hello World"	:string	
# x = 20	:int	
# x = 20.5	:float	
# x = 1j	:complex	
# x = ["apple", "banana", "cherry"]	:list	
# x = ("apple", "banana", "cherry")	:tuple	
# x = range(6)	:range	
# x = {"name" : "John", "age" : 36}	:dict	
# x = {"apple", "banana", "cherry"}	:set	
# x = frozenset({"apple", "banana", "cherry"})	:frozenset	
# x = True	:bool	
# x = b"Hello"	:bytes	
# x = bytearray(5)	:bytearray	
# x = memoryview(bytes(5))	:memoryview	
# x = None	:NoneType	
x = complex(8, 2)
y = True
c = "Harry"
d = None
print(x)
print(y)
#a1 = 9
#print(a + a1)
print("The type of x is ", type(x))
print("The type of y is ", type(y))
print("The type of c is ", type(c))

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)