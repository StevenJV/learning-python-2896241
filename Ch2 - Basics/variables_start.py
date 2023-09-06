#
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# re-declaring a variable works

# to access a member of a sequence type, use []
print(mylist[3])

# use slices to get parts of a sequence
s = slice(5,9)
print("'"+mystr[s]+"'")

# you can use slices to reverse a sequence
s = slice(8,4,-1) #why does this not use same indicies?
print("'"+mystr[s]+"'")

# dictionaries are accessed via keys
print(mydict["one"])

# ERROR: variables of different types cannot be combined

# Global vs. local variables in functions

