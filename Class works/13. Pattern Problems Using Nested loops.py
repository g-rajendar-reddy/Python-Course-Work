'''
# Example: 1
for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()
# Output:
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Example: 2
for row in range(4):
    for col in range(1,6):
        print(col, end=" ")
    print()
# Output:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# Example: 3
for row in range(5):
    for col in range(6):
        print(row+1, end=" ")
    print()
# Output:
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 4 4 4 4 4 4
# 5 5 5 5 5 5

# Example: 4
n = int(input("Enter a size: "))
for i in range(n):
    if i<=n//2:
        print("* " * (i+1))
    else:
        print("* " * (n-i))
# Output:
# Enter a size: 5
# *
# * *
# * * *
# * *
# *

# Example: 5
n = int(input("Enter a size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or col==n-1 or row==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Output:
# Enter a size: 8
# * * * * * * * * 
# *             *
# *             *
# *             *
# * * * * * * * *
# *             *
# *             *
# *             *

# Example: 6
n = int(input("Enter a size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or (row==n-1 and col<n//2) or (col==n//2 and row>=n//2) or (row==n//2 and col>=n//2) or (col==n-1 and row>=n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Output:
# Enter a size: 8
# * * * * * * * * 
# *
# *
# *
# *       * * * *
# *       *     *
# *       *     *
# * * * * *     *







lc = [i for i in range(1,11)]
print(lc)

resl = [i for i in range(1,11) if i%2==0]
print(resl)

namesl = [input("Enter names: ") for i in range(5)]
print(namesl)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10]
# Enter names: raju
# Enter names: kotesh
# Enter names: sai
# Enter names: ram
# Enter names: krishna
# ['raju', 'kotesh', 'sai', 'ram', 'krishna']


s = "hello"
v = 'aeiouAEIOU'
r = [i if i in v else '0' for i in s]
print(r)
# Output:
# ['0', 'e', '0', '0', '0']


dl = {i: i*i for i in range(1,11)}
print(dl)
# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''
