# Input Formatting:
# Python's input() function is used to take input from the user during program execution. By
# default, it returns a string. We often convert the input into int, float, list, tuple, set, or dict as needed.

# 1. String Input
# Use case: Entering a name, email, city, etc.
city = input("Enter Your City Name: ")
print(city)
# Output: Enter Your City Name: hampy 
#         hampy

# 2. Integer Input
# Use case: Age, quantity, mobile number, number of items in cart.
mn = int(input("Enter your mobile number: "))
print(mn)
# Output: Enter your mobile number: 9390617374
#         9390617374

# 3. Float Input
# Use case: Price, temperature, discount, rating.
rating = float(input("Enter your rating: "))
print(rating)
# Output: Enter your rating: 4.5
#         4.5

# 4. Input as List (Space-separated)
# Use case: List of names, marks, or product IDs.
names = input("Enter employee names (space-separated): ").split()
print(names)
# Output: Enter employee names (space-separated): Raju Kotesh Sai
#         ['Raju', 'Kotesh', 'Sai']

# 5. Input as List (Comma-separated)
# Use case: Tags, emails, product categories.
pc = input("Enter product categories (comma-separated): ").split()
print(pc)
# Output: Enter product categories (comma-separated): Milk,Curd,Butter,Ghee,Paneer
#         ['Milk,Curd,Butter,Ghee,Paneer']

# 6. List of Integers
# Use case: Marks, product prices, IDs.
Marks = list(map(int,input("Enter your all subjects marks (space-separated): ").split()))
print(Marks)
# Output: Enter your all subjects marks (space-separated): 80 55 66 75 93 87
#         [80, 55, 66, 75, 93, 87]

# 7. List of Floats
# Use case: Sensor readings, weights, product prices.
weights = list(map(float,input("Enter 5 numbers weights (comma-separated): ").split(',')))
print(weights)
# Output: Enter 5 numbers weights (comma-separated): 5.5,6.1,5.8,5.9,6.2
#         [5.5, 6.1, 5.8, 5.9, 6.2]

# 8. Tuple of Integers
# Use case: Marks, product prices, IDs.
Marks = tuple(map(int,input("Enter your all subjects marks (space-separated): ").split()))
print(Marks)
# Output: Enter your all subjects marks (space-separated): 80 55 66 75 93 87
#         (80, 55, 66, 75, 93, 87)

# 9. Set of Integers
# Use case: Marks, product prices, IDs.
Marks = set(map(int,input("Enter your all subjects marks (space-separated): ").split()))
print(Marks)
# Output: Enter your all subjects marks (space-separated): 80 55 66 75 93 87
#         {80, 55, 66, 75, 93, 87}

# 10. Dictionary Input using eval()
emp_info = eval(input("Enter employee info as a dictionary: "))
print(emp_info)
# Output: Enter employee info as a dictionary: {'empname':'Raju','empid':12323,'empsal':70500}
#         {'empname': 'Raju', 'empid': 12323, 'empsal': 70500}

# 11. Multiple Inputs with Unpacking
# Use case: Login form or payment details.
Username, Password = input("Enter username and password: ").split(',')
print("Username: ",Username)
print("Password: ",Password)
# Output: Enter username and password: raju,123
#         Username:  raju
#         Password:  123


# Output Formatting:

# 1. Basic Examples of print()
# a) Printing Text
print("Hello, World!")    # Output: Hello, World!

# b) Printing Multiple Items
a = 10
b = 2.6
c = "raju"
print('a:',a, 'b:',b, 'c:',c)               # Output: a: 10 b: 2.6 c: raju

# c) Using sep to Change the Separator
print('a:',a, 'b:',b, 'c:',c , sep='---->')      # Output: a:---->10---->b:---->2.6---->c:---->raju

# d) Using end to Control Line Endings
print('a:',a, 'b:',b, 'c:',c , end=' <== THE END')  # Output: a: 10 b: 2.6 c: raju <== THE END

# 2. Printing Special Characters   
# a) Newline (\n)
print("Hello,\nWorld!")    # Output: Hello,
                           #         World!
# b) Tab (\t)
print("Hello,\tWorld!")    # Output: Hello,   World!            

# Output Formatting
# 1. Using Commas (Simple Print Method)
name = "Raju"
age = 25
print("Name:", name, "Age:", age)  # Output: Name: Raju Age: 25 

# 2. Using Modulo Operator (% Formatting)
name = "Raju"
age = 25
print("Name: %s, Age: %d" % (name, age)) # Output: Name: Raju, Age: 25 

# 3. Using f-strings (Formatted String Literals) — Python 3.6+
name = "Raju"
age = 25
score = 92.389
print(f'Name:{name} , Age:{age} , Score:{score:.2f}')  # Output: Name:Raju , Age:25 , Score:92.389

# 4. Using str.format() Method
name = "Raju"
age = 25
family = {'father':'Venkat Reddy', 'mother':'Jyothi'}
print("Name: {}, Age: {}, Family: {}".format(age, name, family)) # Output: Name: 25, Age: Raju, Family: {'father': 'Venkat Reddy', 'mother': 'Jyothi'}











