# 1. Introduction to Tuples
# ● A tuple is an immutable, ordered collection of elements.
# ● Tuples are similar to lists, but once a tuple is created, its contents cannot be changed.
# ● Tuples can store any type of data (int, float, string, list, etc.).
# ● Tuples are faster than lists because they are immutable.

# Tuple Creation Syntax:
t=()
print(t,type(t)) # () <class 'tuple'>
t1 = (1,'raju',True,{},2.3,set())
print(t1,type(t1)) # (1, 'raju', True, {}, 2.3, set()) <class 'tuple'>
t2 = tuple()
print(t2,type(t2)) # () <class 'tuple'>

#  Without parentheses (implicit tuple creation)
t3=1,2,3,4
print(t3,type(t3)) # (1, 2, 3, 4) <class 'tuple'>


# 2. Accessing Tuple Elements
# 2.1 Indexing
I = ('raju','viya','hampy','reddy')
print(I[1])  # viya
print(I[-2]) # hampy

# 2.2 Slicing
I = ('raju','viya','hampy','reddy')
print(I[1:3])   # ('viya', 'hampy')
print(I[:2])    # ('raju', 'viya')
print(I[2:])    # ('hampy', 'reddy')
print(I[::2])   # ('raju', 'hampy')
print(I[-3:-1]) # ('viya', 'hampy')
print(I[::-2])  # ('reddy', 'viya')
print(I[::-1])  # ('reddy', 'hampy', 'viya', 'raju')


# 3. Operations on Tuples
# 3.1 Concatenation
a = (1,2,3)
b = (4,5,6)
print(a+b) # (1, 2, 3, 4, 5, 6)

# 3.2 Repetition
r = ('viya')
print(r*5) # viyaviyaviyaviyaviya

# 3.3 Membership Testing
m = (2,4,6,8)
print(2 in m) # True
print(3 not in m) # True
print(3 in m) # False
 
# 3.4 Tuple Unpacking
p = (7,3,5,1)
a,b,c,d = p
print(d) # 1


# 4. Tuple Methods
a = ('raju','viya','hampy','viya','reddy')
a1 = a.index('hampy')
print(a1) # 2
b1 = a.count('viya') # 2

# 5. Built-in Functions for Tuples
# len(tuple),max(tuple),min(tuple),sum(tuple),tuple(iterable)
f = (1,2,3,4,5)
print(len(f)) # 5
print(min(f)) # 1
print(max(f)) # 5
print(sum(f)) # 15

f1 = tuple([1,3,5,7])
print(f1) # (1, 3, 5, 7)


# 6. Immutability and Tuple Behavior
ud = (1, [2, 3])
ud[1][0] = 50
print(ud) # (1, [50, 3])