
# int
def display(n):
    n+=10
    print(f"Inside: {n}")

n = 10
display(n)
print(f"Outside: {n}")  
# Output: Inside: 20
#          Outside: 10

# float
def display(n):
    n+=10
    print(f"Inside: {n}")

n = 10.2
display(n)
print(f"Outside: {n}")
# Output: Inside: 20.2
#          Outside: 10.2

# str
def display(n):
    n+='Reddy'
    print(f"Inside: {n}")

n = 'Rajendar'
display(n)
print(f"Outside: {n}")
# Output: Inside: RajendarReddy
#         Outside: Rajendar

# tuple
def display(n):
    n+=(4,5)
    print(f"Inside: {n}")

n = (1,2,3)
display(n)
print(f"Outside: {n}")
# Output: Inside: (1, 2, 3, 4, 5)
#         Outside: (1, 2, 3)

# list
def display(n):
    n+=[4,5]
    print(f"Inside: {n}")

n = [1,2,3]
display(n)
print(f"Outside: {n}")
# Output: Inside: [1, 2, 3, 4, 5]
#         Outside: [1, 2, 3, 4, 5]

def display(n):
    n=n.copy()
    n.append(5)
    print(f"Inside: {n}")
# Output: Inside: [1, 2, 3, 5]
#         Outside: [1, 2, 3]


n = [1,2,3]
display(n)
print(f"Outside: {n}")

# set
def display(n):
    n.add(4)
    print(f"Inside: {n}")

n = {1,2,3}
display(n)
print(f"Outside: {n}")
# Output: Inside: {1, 2, 3, 4}
#         Outside: {1, 2, 3, 4}

# dict
def display(n):
    n[4]=5
    print(f"Inside: {n}")

n = {1:2,2:3,3:4}
display(n)
print(f"Outside: {n}")
# Output: Inside: {1: 2, 2: 3, 3: 4, 4: 5}
#         Outside: {1: 2, 2: 3, 3: 4, 4: 5}


# int,float,str,tuple, boolen are pass by value
# list,set,dict are pass by reference


# Recursive
# Example: print 1 to 10
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
        
display(1)    

# Output: 1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9
#        10

# Example: print 10 to 1
def display(n):
    if n==11:
        return
    display(n+1)    
    print(n)

display(1)

# Output: 10
#         9
#         8
#         7
#         6
#         5
#         4
#         3
#         2
#         1

