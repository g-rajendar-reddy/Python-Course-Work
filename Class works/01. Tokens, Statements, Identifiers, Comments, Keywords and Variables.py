# Tokens are the smallest units of a Python program. Python has five types of tokens:
# 1. Keywords – Reserved words in Python (e.g., if, else, while, for, def).
# 2. Identifiers – Names given to variables, functions, and classes.
# 3. Literals – Constant values assigned to variables (e.g., 10, "Hello", 3.14).
# 4. Operators – Symbols that perform operations (e.g., +, -, *, /).
# 5. Punctuators – Symbols like (), {}, [], ,, :,. used for syntax structuring.

# This program calculates the area of a rectangle
length = 10
width = 5
area = length * width
if area > 30:
    print("Large area")
else:
    print("Small area")
# output: Large area

# length - Identifier
# = - Operator
# 10 - Literal
# width - Identifier
# = - Operator
# 5 - Literal
# area - Identifier
# = - Operator
# length - Identifier
# * - Operator
# width - Identifier
# if - Keyword
# area - Identifier
# > - Operator
# 30 - Literal
# : - Punctuator
# print - Identifier
# ( - Punctuator
# "Large area" - Literal
# ) - Punctuator
# else - Keyword
# : - Punctuator
# print - Identifier
# ( - Punctuator
# "Small area" - Literal
# ) - Punctuator
 

# Statements
a = 5         # Assignment statement
print(a)      # Function call statement
# output: 5

# Identifiers
age = 25 # 'age' is an identifier for the variable
def greet(): # 'greet' is an identifier for a function

 my_variable = 10  # Valid identifier
_my123Var = 20   # Valid identifier
Variable = 30     # Valid identifier (case-sensitive)
variable1 = 40   # Valid identifier
#12variable = 50  # Invalid identifier (starts with a digit)

# Comments
# This is a single-line comment
""" This is a multi-line comment
    that spans multiple lines """
def add(a, b):
    return a + b  # Returns the sum of a and b
result = add(3, 4)
print(result)  # output: 7

# Access All Keywords in Python
import keyword
print(keyword.kwlist)      # List of all keywords
print(len(keyword.kwlist)) # Total number of keywords

# Variables
# Must start with a letter (A–Z, a–z) or underscore
Name = "Raju"  
_id = 12
age = 20
# 1st_place = "First"  # Invalid variable name (starts with a digit)
Hampy_reddy8883 = "Instagram id"  # Valid variable name
clg_id = 12345
print(clg_id) # output: 12345   
Clg_id = 54321
print(Clg_id) # output: 54321   case-sensitive
CLG_ID = 67890
print(CLG_ID) # output: 67890   case-sensitive

# Multiple Assignment
a, b, c = 5, 10, 15  # multiple variables in a single line.
print(a,b,c)  # output: 5 10 15
x = y = z = 100 # same value
print(x, y, z) # Output: 100 100 100

# Reassignment
a = 10
a = 20
print(a)  # output: 20

# Swapping Variables
a,b = 1,2
a,b = b,a
print(a,b)  # output: 2 1

# Deleting Variables
x = 10
del x
# print(x)  # This will raise an error since x is deleted
# output: NameError: name 'x' is not defined
