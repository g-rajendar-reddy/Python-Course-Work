# Inheritance
# 1. single level inheritance

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")   

class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")    

obj = B()
obj.feature1()  
obj.feature2()
obj.feature3()
obj.feature4() 

# Output:
# Feature 1 working
# Feature 2 working
# Feature 3 working
# Feature 4 working

# 2. Multi level inheritance
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")   

class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")  

class C(B):
    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")      

obj = C()
obj.feature1()
obj.feature2()   
obj.feature3()
obj.feature4() 
obj.feature5()
obj.feature6() 

# Output:
# Feature 1 working
# Feature 2 working
# Feature 3 working
# Feature 4 working
# Feature 5 working
# Feature 6 working      

# 3. Multiple inheritance  
class A:
    def feature1(self):
        print("Feature 1 working")
   
class B:
    def feature2(self):
        print("Feature 2 working") 

class C(A,B):
    def feature3(self):
        print("Feature 3 working")

obj = C()
obj.feature1()
obj.feature2()
obj.feature3()    

# Output:
# Feature 1 working
# Feature 2 working
# Feature 3 working

# 4. Hierarchical inheritance
class A:
    def feature1(self):
        print("Feature 1 working")
   
class B(A):
    def feature2(self):
        print("Feature 2 working") 

class C(A):
    def feature3(self):
        print("Feature 3 working")

obj = B() 
obj.feature1()

obj = C()
obj.feature1()

# Output:
# Feature 1 working
# Feature 1 working


# 5. Constructor in inheritance
class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("Feature 1 working")
   
class B(A):
    def __init__(self):
        super().__init__()
        print("init B")
    def feature2(self):
        print("Feature 2 working") 

obj = B()

# Output:
# init A
# init B     





