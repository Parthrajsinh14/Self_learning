print("hello")
#to run python filname.py


 # here in python we use indentation like space or tab instead of braces in loop or if stat

if 5>2:
    print("5 is greater than 2")

#wrong indentation will give error
# if 5>2:
# print("5 is greater than 2")


#and also we does not declare variable type in python

# single line comment

""" multi line comment """

"""
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.


age = 36
txt = f"My name is John, I am {age}"
print(txt)

"""


"""
Escape Characters
Escape characters are used in strings to insert characters that are illegal in a string.
Code    	Result	
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	  Octal value	
\xhh	  Hex value
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	  Octal value	
\xhh	  Hex value

"""

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

"""


"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
is and is not are the identity operators in Python.
x = ["apple", "banana"]   

y = ["apple", "banana"]
print(x is y)  # False, because they are not the same object
print(x is not y)  # True, because they are not the same object



Membership operators are used to test if a sequence is presented in an object:
it use in and not in operators.
x = ["apple", "banana"]
print("banana" in x)  # True, because a sequence with the value "banana" is in the list
print("pineapple" not in x)  # True, because a sequence with the value "pineapple" is NOT in the list

"""





