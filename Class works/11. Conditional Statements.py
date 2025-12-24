# 1. if Statement
a = 10
if a > 5:
    print("a is greater than 5")
# Output: a is greater than 5

# 2. if-else Statement
b = 3
if b % 2 == 0:
    print("b is even")
else:
    print("b is odd")
# Output: b is odd

# 3. if-elif-else Statement
c = 15
if c < 10:
    print("c is less than 10")
elif c < 20:
    print("c is less than 20")
else:
    print("c is greater than or equal to 20")
# Output: c is less than 20

# 4. Nested if Statement
d = 8
if d > 0:
    if d < 10:
        print("d is a positive single-digit number")
    else:
        print("d is a positive number with multiple digits")
else:
    print("d is not a positive number")
# Output: d is a positive single-digit number


