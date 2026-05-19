# In Python, we move from processes (procedural programming) to objects (object-oriented programming) mainly to handle complex, real-world problems better.
# 1. Better organization, 2. Real-world modeling, 3. Reusability, 4. Maintainability, 5. Scalability, 6. Security
# Example:
# Procedural approach
balance = 5000

def deposit(amount):
    global balance
    balance += amount
deposit(amount=400)
print(balance)

# Object-oriented approach
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

a1 = Account(5000)
a1.deposit(amount=400)
print(a1.balance)

# Class
# A class is a blueprint for creating objects.
# It defines the attributes (variables) and methods (functions) that the objects will have. 
# Example: E-commerce Product Class 
# Step 1: Define a class 
class Product:
# Attributes (data or variables)
    Name = 'Milk'
    Quantity = '1 lit'
    Price = 80
# Methods (functions)
    def display_info(self):
        print(f"Product:{self.Name}, Quantity:{self.Quantity}, Price:{self.Price}")

# Objects
# An object is an instance of a class.
# You can create multiple objects from a single class. 
# Step 2: Create objects of the Product class    
p1 = Product() # Object 1
p2 = Product() # Object 2
# Access attributes and methods
p1.display_info()
p2.display_info()
# Output:
# Product:Milk, Quantity:1 lit, Price:80
# Product:Milk, Quantity:1 lit, Price:80

# Attributes 
# Attributes are variables that store the state of an object.
# Example: Modifying Attributes
p1.Name = "Buttermilk"
p1.display_info()
# Output : Product:Buttermilk, Quantity:1 lit, Price:80

# 1. Types of Attributes 
# (a) Instance Attributes : change  varible data
class Product:
    def __init__(self,Name,Quality,Price):
        self.Name = Name  # Instance Attribute 
        self.Quality = Quality
        self.Price = Price
D1 = Product('Dell Laptop','Good',90000)  
print(D1.Name)
# Output: Dell Laptop

# Example2

class Product:
    def __init__(self,Name,Quality,Price):
        self.Name = Name  # Instance Attribute 
        self.Quality = Quality
        self.Price = Price
    def display_all(self):
        print(self.Name,self.Quality,self.Price)    
D1 = Product('Dell Laptop','Good',90000)  
D1.display_all()
# Output: Dell Laptop Good 90000
     
# (b) Class Attributes : can not change varible data
class Product:
    Discount = 10    # Class Attribute
    def __init__(self,name,price):
        self.name = name
        self.price = price
# Accessing class attribute
print(Product.Discount)   # Output: 10


# Methods 
# Methods are functions that belong to a class.
# They define the behavior of the object.
# Example: Adding a Method
# Step 4: Add a method to calculate total price
class Product:
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_info(self):
        print(f"Product:{self.name}, Price:{self.price}, Quantity:{self.quantity}") 
    def calculate_total_price(self):
        return self.price * self.quantity

# Create an object
d1 = Product('tablet',350,5)   
d1.display_info()
print(f"Total price: {d1.calculate_total_price()}")        
        
# Types of Methods
# (a) Instance Methods 
# Work with instance attributes (self). 
# Can modify instance-specific data.

class student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        print(f"Average Marks in 3 subjects = {self.m1+self.m2+self.m3/3}")    


s1 = student(87,69,90) 
s2 = student(75,82,79)
s1.avg()
s2.avg()    
print(s1.m1)
print(s1.m2)
print(s1.m2)   

# (b) Class Methods 
# Use @classmethod decorator. 
# Work with class attributes using cls.           

class student:
    college = 'sri gayatri'
    
    @classmethod
    def getcollege(cls):
        return cls.college        

# class method accesses
print(student.getcollege())


# (c) Static Methods 
# Use @staticmethod decorator. 
# Independent of both instance and class attributes. 
# Used for utility functions.
# Example 1:
class student:
    @staticmethod
    def info():
        print("This is student class")

student.info() 

# Example 2:
class Product: 
    @staticmethod 
    def is_expensive(price): 
        return price > 3000
print(Product.is_expensive(5000))    # True
print(Product.is_expensive(2000))    # False

# All Method in one Example
class student:

    college = 'sri gayatri'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        print(f"Average Marks in 3 subjects = {self.m1+self.m2+self.m3/3}")   

    @classmethod
    def getcollege(cls):
        return cls.college      
    
    @staticmethod
    def info():
        print("This is student class")


s1 = student(87,69,90) 
s2 = student(75,82,79)
s1.avg()
s2.avg()    
print(s1.m1)
print(s1.m2)
print(s1.m2)   

# class method accesses
print(student.getcollege())

# static method accesses
student.info() 