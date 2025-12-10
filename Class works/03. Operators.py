# 1. Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)          # Addition: 13
print("Subtraction:", a - b)       # Subtraction: 7     
print("Multiplication:", a * b)    # Multiplication: 30
print("Division:", a / b)          # Division: 3.333333333333
print("Floor Division:", a // b)   # Floor Division: 3
print("Modulus:", a % b)           # Modulus: 1
print("Exponentiation:", a ** b)   # Exponentiation: 1000

# 2. Comparison Operators
print("Equal:", a == b)            # Equal: False
print("Not Equal:", a != b)        # Not Equal: True    
print("Greater Than:", a > b)      # Greater Than: True
print("Less Than:", a < b)         # Less Than: False
print("Greater Than or Equal:", a >= b)  # Greater Than or Equal: True
print("Less Than or Equal:", a <= b)     # Less Than or Equal: False

# 3. Assignment Operators
c = a
print("Initial c:", c)              # Initial c: 10
c += b
print("c after += b:", c)           # c after += b: 13
c *= b
print("c after *= b:", c)           # c after *= b: 39
c -= b
print("c after -= b:", c)           # c after -= b: 36
c /= b
print("c after /= b:", c)           # c after /= b: 12.0
c %= b
print("c after %= b:", c)           # c after %= b: 0.0
c **= 2
print("c after **= 2:", c)          # c after **= 2: 0.0
c //= 2
print("c after //= 2:", c)          # c after //= 2: 0.0

# 4. Logical Operators
x = True
y = False
print("x and y:", x and y)         # x and y: False
print("x or y:", x or y)           # x or y: True
print("not x:", not x)              # not x: False
print("not y:", not y)              # not y: True

# 5. Membership Operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)       # 3 in my_list: True
print("6 in my_list:", 6 in my_list)       # 6 in my_list: False
print("3 not in my_list:", 3 not in my_list) # 3 not in my_list: False
print("6 not in my_list:", 6 not in my_list) # 6 not in my_list: True   

# 6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)             # a is b: True
print("a is c:", a is c)             # a is c: False
print("a is not c:", a is not c)     # a is not c: True
print("a is not b:", a is not b)     # a is not b: False

# 7. Bitwise Operators
p = 5  # 0b0101
q = 3  # 0b0011
print("p & q:", p & q)               # p & q: 1 (0b0001)
print("p | q:", p | q)               # p | q: 7 (0b0111)
print("p ^ q:", p ^ q)               # p ^ q: 6 (0b0110)
print("~p:", ~p)                     # ~p: -6 (two's complement)
print("p << 1:", p << 1)             # p << 1: 10 (0b1010)
print("p >> 1:", p >> 1)             # p >> 1: 2 (0b0010)
# End of Operators Example


