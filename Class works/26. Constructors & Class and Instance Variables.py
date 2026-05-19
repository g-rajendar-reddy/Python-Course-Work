# 1. self in Instance Methods 
# Used to access instance attributes inside the class. 
# Every instance method must include self as the first parameter. 
class Product: 
    def __init__(self, name, price): 
        self.name = name  # Assigning instance attributes 
        self.price = price 
    def display_info(self): 
        print(f"Product: {self.name}, Price: {self.price}") 
# Creating objects 
p1 = Product("Laptop", 50000) 
p2 = Product("Phone", 20000) 
# Calling instance method 
p1.display_info()  # Output: Product: Laptop, Price: 50000 
p2.display_info()  # Output: Product: Phone, Price: 20000 


# 2. self Helps in Modifying Instance Attributes 
# We can update attributes for each object using self.
class Product: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 
 
    def apply_discount(self, discount): 
        self.price -= self.price * (discount / 100)  # Modifying instance attribute 
 
p1 = Product("Laptop", 50000) 
p1.apply_discount(10)  # Applying 10% discount 
 
print(p1.price)  # Output: 45000 


# 3. self is Not a Keyword 
# self is just a naming convention; you can use any other name, but it's not recommended. 
class Product: 
    def __init__(xyz, name, price):  # Using 'xyz' instead of 'self' 
        xyz.name = name 
        xyz.price = price 
 
    def display_info(abc):  # Using 'abc' instead of 'self' 
        print(f"Product: {abc.name}, Price: {abc.price}") 
 
p1 = Product("Tablet", 30000) 
p1.display_info()  # Output: Product: Tablet, Price: 30000 

# 4. self vs. Class Attributes (cls) 
# self refers to instance attributes. 
# cls (used in @classmethod) refers to class attributes.


# Constructors 
# A constructor is a special method (`__init__`) that is automatically called when an object is created. 
# It is used to initialize the object's attributes. 

class Product: 
# Constructor 
    def __init__(self, name, price, quantity): 
        self.name = name 
        self.price = price 
        self.quantity = quantity 
    def display_info(self): 
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}") 
# Create an object 
product1 = Product("Headphones", 1500, 10) 
product1.display_info()  # Output: Product: Headphones, Price: 1500, Quantity: 10