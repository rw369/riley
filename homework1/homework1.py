#File: homework1. py

# --- Variables and Data Types --- 

a = 10
b = 1.5
c = 3j
d = "hello"
e = [1,2,3]
f = {"name": "Ellen", "favorite fruit": "strawberry"}
g = (1,2)
h = ["apple", "banana", "strawberry"]
i = True
j = None
k = [True, "blue", 12]
l = str(14)
m = 1e4
"""
1.) 9 different data types
2.) Integery, Float, Complex, String, List, Dictionary, Tuple, Boolean, and NoneType
3.) b-m, d-l, e-h-k
4.) l is not an integer because the str() command converts whatever is in the () to a string
5.) Another data type is a set, which is used to store multiple items in a single variable, and it is
a collection that is unordered, unindexed, and you cannot change set items, but you can add and remove set items
"""


print(a)
print(type(a)) #a is an integer, which is a whole number, no decimals

print(b)
print(type(b)) #b is a float, which is a number with decimals

print(c)
print(type(c)) #c is a complex, which is a number consisting of a real part and imaginary part

print(d)
print(type(d)) #d is a string, which is a sequence of characters in quotations

print(e)
print(type(e)) #e is a list, which is a data structure storing multiple items into a single variable

print(f)
print(type(f)) #f is a dictionary, which is a datat structure that stores values in key: value pairs

print(g)
print(type(g)) #g is a tuple, which stores multiple items in one variable like a list, but the elements of a tuple cannot be changed like a list

print(h)
print(type(h)) #h is a list, which is a data structure storing multiple items into a single variable

print(i)
print(type(i)) #i is a boolean, which is a value that is either true or false

print(j)
print(type(j)) #j is a NoneType, which is the data type for the None object, which indicates no value

print(k)
print(type(k)) #k is a list, which is a data structure storing multiple items into a single variable

print(l)
print(type(l)) #l is a string, which is a sequence of characters in quotations

print(m)
print(type(m)) #m is a float, which is a number with decimals



# --- Booleans ---

print(10>9) #True, as 10 is greater than 9
print(10==9) #False, as 10 != 9
print(10<=9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, as this is a non-empty string converted to a boolean
print(bool(123)) #True, as this is a non-zero int converted to a boolean
print(bool(["apple", "cherry", "banana"])) #True, non-empty list converted to boolean
print(bool(True)) #True, true is true
print(bool(False)) #False, false is false
print(bool(0)) #False, 0 converted to boolean
print(bool("")) #False, empty string converted to boolean
print(bool(" ")) #True, non-empty string converted to boolean
print(bool(())) #False, empty tuple converted to boolean
print(bool([])) #False, empty list converted to boolean
print(bool({})) #False, empty set converted to boolean
print(bool(True and False)) #False, the first value is true but the second value is false so the and operator returns false
print(bool(True and True)) #True, both values are true so and operator returns true
print(bool(False and False)) #False, the first value is false so the and operator returns false
print(bool(True or False)) #True, since the first value is true the or operator returns true
print(bool(True or True)) #True, since the first value is true the or operator returns true
print(bool(False or False)) #False, since the first value is false the or operator returns the second value which is false
print(bool(not(False))) #True, the not operator inverts the boolean value, which is false, so it returns true
print(bool(not(True))) #False, the not operator inverts the boolean value, which is true, so it returns false
"""
1.) The main pattern I noticed was when converting other data types to boolean, what determins if it is 
true or false is if it is empty, 0, or the equaivalent for other data types. In these cases it is false,
but if the value is anything other than empty, 0, etc it will be true.
2.) print(bool("abc")) surprised me at first, I thought it would be false as it was a string but now I 
understand why it's true
3.) print(bool(False or True))
This will be True because the or operator will read the first value as false, and return the second value 
which is true
4.) print(bool(0.0))
This will be false because a float with value 0.0 is false when converted to a boolean value
"""


# --- Operators ---

print(10+5) #15, performs addition
print(10-5) #5, performs subtratction
print(2*4) #8, performs multipulcation
print(6/3) #2.0, performs division and outputs value as a float
print(5%2) #1, performs division and outputs the remainder
print(3**2) #9, raises the first number to the power of the second number
print(15//2) #7, performs division, rounding the output down to nearest lower integer, outputting an integer
print(5==2) #False, evaluates if the two values are equal
print(10!=10) #False, evaluates if the two values do not equal each other
print(2<5) #True, evaluates if the first value is less than the second
print(12>5) #True, evaluates if the first value is greater than the second
print(5<=6) #True, evaluates if the first value is less than or equal to the second
print(1>=10) #False, evaluates if the first value is greater than or equal to the second

x = 5
print(x) #5, this is the value we assigned x

x += 5
print(x) #10, this adds the number to x and assigns the resulting value to x

x -= 4
print(x) #6, this subtracts the number to x and assigns the resulting value to x

x *= 3
print(x) #18, this multiplies the number to x and assigns the resulting value to x

"""
Logical Operators:
1.) The and operator returns true if both values are true, otherwise it returns false
print(bool(True and True)) = True
print(bool(False and True)) = False
2.) The or operator returns true if either of the values are true, otherwise it returns false
print(bool(True or False)) = True
print(bool(False or False)) = False
3.) The not operator returns the opposite true or false value of the value it reads
print(bool(not(False))) = True
print(bool(not(True))) = False
"""

"""
More Questions:
1.) / will perform regular division and always returns a float value, while // performs division
and rounds down to an integer, and always returns an integer value
2.) % performs regular divisoin then returns the remainder, while // performs division and rounds down
to the next lowest integer
3.) You would use the % operator
print(17%4) = 1
4.) Assignment operators perform an operation on a variable, then assign the resulting value to the 
variable
"""


# --- Strings ---

my_string = "hello"
print(my_string) #prints "hello"
print(my_string[0]) #prints the 0th character of my_string which is h
print(my_string[1]) #prints the 1st character of my_string which is e
print(my_string[2]) #prints the 2nd character of my_string which is l
print(my_string[3]) #prints the 3rd character of my_string which is l
print(my_string[4]) #prints the 4th character of my_string which is o
print(my_string[-1]) #prints the -1st character of my_string, which is o
print(my_string[1:3]) #prints the 1st and 3rd characters of my_string which is e and l
print(my_string[0:5:2]) #prints the 0th, 5th, and 2nd characters of my_string which is h, l, and o
print(len(my_string)) #prints how many characters are in my_string which is 5
print(my_string + "goodbye") #adds the string "goodbye" to my_string resulting in it printing the result hellogoodbye
print(my_string * 7) #multiplies my_string by 7, printing 7 my_string's in a row

"""
1.) Slicing is extracting a portion from a sequence like this string
I used slicing when printing my_string[1:3] and my_string[0:5:2]
"""
#2.)
name = "Oski"
print("Hello, my name is", name)

#3.)
name = "Oski"
print(f"Hello, my name is {name}")

"""
4.) The output of the last two print statements is the exact same, however the f string
allows the string varialbe name to go inside the string we are printing, rather than having it separated
and just added on to the string at the end.
"""


# --- Terminal Commands ---

"""

"""