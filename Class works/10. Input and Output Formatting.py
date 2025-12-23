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

