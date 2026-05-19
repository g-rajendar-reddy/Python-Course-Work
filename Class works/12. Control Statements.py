# 1. for loop
# Example:1
a = ['apple', 'banana', 'cherry']
for i in a:
    print(i.capitalize(), end=' ')
# Output: Apple Banana Cherry

# Example:2
data = {'name': 'John', 'age': 25, 'city': 'New York'}
for i in data:
    print(f'{i} : {data[i]}')
# Output: name : John
#         age : 25
#         city : New York

# Example:3
full_name = "Gajjela Rajendar Reddy"
vol = 'aeiouAEIOU'
for i in full_name:
    if i in vol:
        print(i, end=' ')
# Output: a e a e a e e

# Example:4
full_name = "Gajjela Rajendar Reddy"
vol = 'aeiouAEIOU'
for i in full_name:
    if i not in vol:
        print(i, end=' ')
# Output: G j j l  R j n d r  R d d y

# Example:5
for i in range(1, 11):
    print(i, end='  ')
# Output: 1  2  3  4  5  6  7  8  9  10

# Example:6
for i in range(1,11,2):
    print(i, end='  ')
# Output: 1  3  5  7  9

# Example:7
n = int(input("Enter a Table number: "))
for i in range(1,11):
    print(f'{n}*{i} = {n*i}')
# Output: Enter a Table number: 5
# 5*1 = 5
# 5*2 = 10
# 5*3 = 15
# 5*4 = 20
# 5*5 = 25
# 5*6 = 30
# 5*7 = 35
# 5*8 = 40
# 5*9 = 45
# 5*10 = 50 

# Example:7
l = ['apple', 'banana', 'cherry']
for i in range(len(l)):
    print(i+1,l[i])

# Example:8
l = ['apple', 'banana', 'cherry']
for i,v in enumerate(l):
    print(i+1,'-------->',v)
# Output: 1 --------> apple
#         2 --------> banana    
#         3 --------> cherry


# Fibonacci Series Program
n = int(input("Enter number of terms: "))

a, b = 0, 1
print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c

# Prime Numbers
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")





# 2. while loop
# Example:1
i = 1
while i<=10:
    print(i, end='  ')
    i+=1
# Output: 1  2  3  4  5  6  7  8  9  10

# Example:2    
i = 10
while i>0:
    print(i, end='  ')
    i-=1
# Output: 10  9  8  7  6  5  4  3  2  1

# Example:3
l = ['apple', 'banana', 'cherry']
i = 0
while i < len(l):
    print(i,l[i])
    i+=1
# Output: 0 apple
#         1 banana
#         2 cherry

# Example:4
full_name = "Gajjela Rajendar Reddy"
i = 0
while i < len(full_name):
    print(i,full_name[i], end=' ')
    i+=1
# Output: 0 G 1 a 2 j 3 j 4 e 5 l 6 a 7   8 R 9 a 10 j 11 e 12 n 13 d 14 a 15 r 16   17 R 18 e 19 d 20 d 21 y


# pass
for i in range(5):
    pass  # Placeholder for future code
# Output: (No output, as pass does nothing)

# break
for i in range(1, 11):
    if i == 6:
        break  # Exit the loop when i is 6
    print(i, end=' ')
# Output: 1 2 3 4 5

# continue
for i in range(1, 11):
    if i == 6:
        continue # Skip the rest of the loop when i is 6  
    print(i, end=' ')
# Output: 1 2 3 4 5 7 8 9 10


# FOR LOOP WITH ELSE
Example:1
Products = ['Milk','Curd','Butter','Cheese','Ghee','Paneer']
Product = input("Enter the product name to search: ") 
for item in Products:
    if item == Product:
        print(f'{Product} is available in the store.')
        break
else:
    print(f'{Product} is not available in the store.')

Example:2
Data = {
       1:{'Product':'Milk', 'Price':80},
       2:{'Product':'Curd', 'Price':90},
       3:{'Product':'Butter', 'Price':250},
       4:{'Product':'Cheese', 'Price':300},
       5:{'Product':'Ghee', 'Price':500},
       6:{'Product':'Paneer', 'Price':600}
       }

for i in Data:
    print(f"{i}. {Data[i] ['Product']} ---> ₹{Data[i]['Price']}")

Bag = tuple(map(int,input("Enter the Products: ").split()))

total = 0
print("Bill".center(30,'-'))
s=set()
for i in Bag:
    if i not in s:
        print(f"{Data[i] ['Product']} * {Bag.count(i)} ---> ₹{Data[i]['Price']}")
        total+= Data[i]['Price'] * Bag.count(i)
    s.add(i)    

print(f"Total Amount: {total}")    


# WHILE LOOP WITH ELSE




