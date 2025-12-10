#int (Immutable Objects)
a=25
print(a,type(a),id(a)) # 25 <class 'int'> 140716707548344

#float (Immutable Objects)
b=25.5
print(b,type(b),id(b)) # 25.5 <class 'float'> 2255501001488
b1=4e2
print(b1,type(b1),id(b1)) # 400.0 <class 'float'> 2255497047856
b2=4e-2 
print(b2,type(b2),id(b2)) # 0.04 <class 'float'> 2255501001136

#bool (Immutable Objects)
c=True
print(c,type(c),id(c)) # True <class 'bool'> 140716706746896
c1=False # False <class 'bool'> 140716706746928
print(c1,type(c1),id(c1))
print(True+True) # 2
print(True+False) # 1
print(False+False) # 0

#complex (Immutable Objects)
d=3+4j
print(d,type(d),id(d))  # (3+4j) <class 'complex'> 2255501001776
d1=2j  
print(d1,type(d1),id(d1)) # 2j <class 'complex'> 2255501001264
d2=5-0j
print(d2,type(d2),id(d2))  # (5+0j) <class 'complex'> 2255501001808
dd=d1*d2
print(dd,type(dd),id(dd))  # 10j <class 'complex'> 2255501003760
d3=complex(2,3)
print(d3,type(d3),id(d3))  # (2+3j) <class 'complex'> 2255501003696
d4=2.3+4.5j
print(d4,type(d4),id(d4))  # (2.3+4.5j) <class 'complex'> 2255501001840
print(d.real) # 3.0
print(d.imag) # 4.0

#str (Immutable Objects)
e="Hello"
print(e,type(e),id(e)) # Hello <class 'str'> 2255501001920
e1='Welcome'
print(e1,type(e1),id(e1)) # Welcome <class 'str'> 2255501001984
e2='''Python Programming
is fun'''
print(e2,type(e2),id(e2)) # Python Programming is fun <class 'str'> 2255497606000
e3="""Data Types in Python
are important"""
print(e3,type(e3),id(e3)) # Data Types in Python are important <class 'str'> 2255497606032
e4="Hello 'Python' Programming"
print(e4,type(e4),id(e4)) # Hello 'Python' Programming <class 'str'> 2255501002048
e5='Hello "Python" Programming'
print(e5,type(e5),id(e5)) # Hello "Python" Programming <class 'str'> 2255501002112
e6="Hello \nPython"
print(e6,type(e6),id(e6))  # Hello 
                           # Python <class 'str'> 2255501002176
e7="Hello\tPython"
print(e7,type(e7),id(e7))  # Hello	Python <class 'str'> 2255501002240
e8="C:\\Users\\Admin"
print(e8,type(e8),id(e8))  # C:\Users\Admin <class 'str'> 2255501002304

#bytes (Immutable Objects) range of (0,256) bytes data type stores the data from 0 to 255 (256-1)
f=[112,209,254,255]
b=bytes(f)  
print(b,type(b)) # b'p\xd1\xfe\xff' <class 'bytes'>

#bytearray (Mutable Objects) range of (0,256) bytes data type stores the data from 0 to 255 (256-1)
ba=bytearray(f)
print(ba,type(ba)) # bytearray(b'p\xd1\xfe\xff') <class 'bytearray'>
ba[0]=120  
print(ba)  # bytearray(b'x\xd1\xfe\xff')

#range (Immutable Objects)
r=range(10)
print(r,type(r))  # range(0, 10) <class 'range'>
for i in r:
    print(i,end=" ") # 0 1 2 3 4 5 6 7 8 9

r1=range(5,15)
print("\n",r1,type(r1)) # range(5, 15) <class 'range'>
for i in r1:
    print(i,end=" ")  # 5 6 7 8 9 10 11 12 13 14

r2=range(1,20,3)
print("\n",r2,type(r2))  # range(1, 20, 3) <class 'range'>
for i in r2:
    print(i,end=" ")   # 1 4 7 10 13 16 19

# List (Mutable)
L=[10,20,30,40,50]
print(L,type(L))  # [10, 20, 30, 40, 50] <class 'list'>
L[0]=100
print(L)  # [100, 20, 30, 40, 50]
L.append(60)
print(L)  # [100, 20, 30, 40, 50, 60]
s="MISSISSIPPI"
L1=list(s)
print(L1)  # ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'P', 'I']

L2=L.copy() # Shallow Copy
print(L2)  # [100, 20, 30, 40, 50, 60]

L3=L1 # Deep Copy
print(L3)  # ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'P', 'I']

# Tuple (Immutable)
T=(10,20,30,40,50)
print(T,type(T))  # (10, 20, 30, 40, 50) <class 'tuple'>
s="MISSISSIPPI"
T1=tuple(s)
print(T1)   # ('M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'P', 'I')
T2=T[1]
print(T2)   # 20
cou=s.count('S')
print(cou)  # 4

# Set (Mutable and Immutable)
S={10,20,30,40,50}
print(S,type(S))  # {10, 20, 30, 40, 50} <class 'set'>
S1="23"
S2=set(S1)
print(S2,type(S2))  # {'2', '3'} <class 'set'>
S.add(660)
print(S)  # {40, 10, 660, 50, 20, 30}

# Frozenset (Immutable)
f="hello"
f1=frozenset(f)
print(f1,type(f1))  # frozenset({'h', 'e', 'o', 'l'}) <class 'frozenset'>
f2=frozenset({2,3})
f3=frozenset([10,20,30])
f4=frozenset((5,6,7))
print(f2,f3,f4,type(f2))  # frozenset({2, 3}) frozenset({10, 20, 30}) frozenset({5, 6, 7}) <class 'frozenset'>

# Dictionary (Mutable)
D={"A":1,"B":2,"C":3}
print(D,type(D))    # {'A': 1, 'B': 2, 'C': 3} <class 'dict'>
lis=[("A",1),("B",2),("C",3)]   
D1=dict(lis)
print(D1,type(D1))  # {'A': 1, 'B': 2, 'C': 3} <class 'dict'>

D["D"]=4
print(D)    # {'A': 1, 'B': 2, 'C': 3, 'D': 4}

D1.update({"E":5})
print(D1)   # {'A': 1, 'B': 2, 'C': 3, 'E': 5}

# NoneType (Immutable)
N=None
print(N,type(N),id(N))  # None <class 'NoneType'> 140716706747184