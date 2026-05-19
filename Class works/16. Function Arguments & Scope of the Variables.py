'''# Function Arguments
# 1. Positional Arguments
def display(uname,email,pwd):
    print(f"Username: {uname}\nEmail: {email}\nPwd: {pwd}")

# display('Viya', 'viya@gmail.com','Viya@123')  

# 2. Keyword Arguments
display(email="raju@gmail.com", pwd="Raju@8883", uname="Raju")

# 3. Default Arguments
def greet(name, age=25):
    print(f"Name: {name}\nAge: {age}")

greet("Srinivas Reddy")   # default age = 18

'''
# 4. Variable-Length Arguments
