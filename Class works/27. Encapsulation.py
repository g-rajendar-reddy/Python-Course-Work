
# 1. Encapsulation 
# Encapsulation is one of the key principles of OOP. It attributes (varibles) and methods (functions) into a single unit (class) while 
# restricting direct access to some data to ensure security and maintainability. 
# Why Encapsulation?: Data Security, Code Maintainability, Controlled Access, Data Integrity

# 2. Types of Attributes in Encapsulation 
# Python allows three levels of access control for attributes: 
# 1. Public (username): Can be accessed and modified from anywhere. 
# 2. Protected (_otp): Meant for internal use within the class and subclasses but still accessible. 
# 3. Private (__password): Restricted access within the class only

# 3. Public Attributes
# Example of a Public Attribute (username) 
class user:
    def __init__(self,username):
        self.username = username    # Public attribute

# Creating an object
user1 = user('hampy8883')

# Accessing public attribute
print(user1.username) # Output: hampy8883

# Modifying public attribute
user1.username = 'raju123'
print(user1.username)  # Output: raju123

# 4. Protected Attributes
class user:
    def __init__(self,username,otp):
        self.username = username   # Public attribute
        self._otp = otp     # Protected attribute

# Creating an object 
user1 = user('viya1805',3105)
# Accessing protected attribute (not recommended, but works) 
print(user1._otp)   # 3105      
# Modifying protected attribute
user1._otp = 8883
print(user1._otp)  # 8883
 
# Using Protected Attributes in a Subclass 
class Admin(user):
    def show_otp(self):
        return f"Admin can see OTP: {self._otp}" 
A = Admin('ram829','7284')    
print(A.show_otp())
# Output : Admin can see OTP: 7284
# Note: Protected attributes should ideally be modified using setter methods instead of direct modification. 

# 5. Private Attributes
# Example of a Private Attribute (__password) 
class user:
    def __init__(self,username,password):
        self.username = username # Public attribute
        self.__password = password  # Private attribute

# Creating an object
user1 = user('madam44','Class@123')
# Trying to access private attribute directly (will cause an error) 
# print(user1.__password) # AttributeError: 'User' object has no attribute '__password'

# Accessing Private Attributes Using Getter and Setter Methods
class User: 
    def __init__(self, username, password): 
        self.username = username   
        self.__password = password  
# Getter method to retrieve password (returns masked password) 
    def get_password(self):
        return self.__password
# Setter method to update password with validation
    def set_password(self,new_password):
        if len(new_password)<6:
            print("Error: Password must be at least 6 characters long.")
        else:
            self.__password = new_password
            print("Password updated successfully.") 


obj1 = User('madam44','Class@123')    
print(obj1.get_password()) # Class@123  

obj1.set_password('Roc26') # Error: Password must be at least 6 characters long.
obj1.set_password('Roc26728') # Password updated successfully.





# 7. Complete Encapsulation Example (Public, Protected, and Private Attributes) 
class User: 
    def __init__(self, username, password, otp): 
        self.username = username  # Public attribute 
        self._otp = otp  # Protected attribute 
        self.__password = password  # Private attribute 
 
    # Getter for password 
    def get_password(self): 
        return self.__password 
 
    # Setter for password 
    def set_password(self, new_password): 
        if len(new_password) < 6: 
            print("Error: Password must be at least 6 characters long.") 
        else: 
            self.__password = new_password 
            print("Password updated successfully.") 
 
    # Getter for OTP 
    def get_otp(self): 
        return self._otp   
 
    # Setter for OTP 
    def set_otp(self, new_otp): 
        self._otp = new_otp 
        print("OTP updated successfully.") 
 
# Creating a user object 
user1 = User("john_doe", "secure123", "123456") 
 
# Accessing and modifying public attribute 
print(user1.username)  # Output: john_doe 
user1.username = "jane_doe" 
print(user1.username)  # Output: jane_doe 
 
# Accessing protected attribute 
print(user1.get_otp())   
user1.set_otp("987654")   
print(user1.get_otp())   
# Accessing private attribute via getter 
print(user1.get_password())   
# Updating private attribute via setter 
user1.set_password("newPass123")  