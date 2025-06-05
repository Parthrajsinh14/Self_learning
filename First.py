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
"""
in python we use match instead of switch and use case as it is

match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case _:
        print("x is something else")


day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

"""

#LOOPS 
"""
in python we have ony two types of loop while and for loop
while loop

i = 1
while i < 6:
  print(i)
  i += 1


  With the break statement we can stop the loop even if the while condition is true

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1  


  With the continue statement we can stop the current iteration, and continue with the next

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
"""
"""
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.


"""



#Functions
"""
def my_function():
    print("Hello from a function")

my_function()

def my_function(x):
  return 5 * x

print(my_function(3))



You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
"""

#Lambda Functions
"""
lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


#here n = 2 and a=11
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

"""