'''
# Polymorphism
# Same function works with different objects.
# Duck Typing
class Car:
    def move(self):
        print("Car is moving")

class Bike:
    def move(self):
        print("Bike is moving")

class travel:        
    def transport(self,vehicle):
        vehicle.move()

vehicle1 = Car()
vehicle2 = Bike()

obj = travel()
obj.transport(vehicle1)
obj.transport(vehicle2)

# Operator Overloading
class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self, other):
        return self.num+other.num
    def __sub__(self, other):
        return self.num-other.num  
    
n1 = Number(20)
n2 = Number(50)

print(n1 + n2)   # Calls __add__()
print(n1 - n2)   # Calls __sub__()
'''
# Method Overloading



# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

a = Dog()
a.sound()


