# 1. Basic Features of Lists
# ● Ordered: Lists maintain the order of elements.
# ● Mutable: Elements can be modified after creation.
# ● Indexed: Elements can be accessed using an index (starting from 0).
# ● Allow Duplicates: Lists can contain duplicate values.
# ● Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).
# ● Dynamic: Size is not fixed; elements can be added or removed dynamically.
# Example of a list with various data types and duplicate values
a=[2,1,5,5,5,"raju",True,None,5.6,(1,2)]
print(a)
# Output: [2, 1, 5, 5, 5, 'raju', True, None, 5.6, (1, 2)]


# 2. Creating Lists
# 2.1 Empty List
a=[]  # Empty list
b = list() # Empty list using list() constructor

# 2.2 List with Elements
n = [1, 2, 3, 4, 5]  # List of integers
s = ["apple", "banana", "cherry"]  # List of strings
m = [1, "apple", 3.14, True]  # Heterogeneous list

# 2.3 List with Nested Lists
ln = [1, 2, [3, 4], [5, 6]]  # List containing nested lists

# 2.4 List using list() Constructor
c = list((1, 2, 3))  # Creating a list from a tuple
d = list("hello")  # Creating a list from a string
print(c) # [1, 2, 3]
print(d) # ['h', 'e', 'l', 'l', 'o']


# 3. Accessing Elements in a List
# 3.1 Using Indexing (Positive & Negative)
I = ['raju','hampy','gajjela','viya','reddy']
print(I[0])    # Output: 'raju' (first element)
print(I[2])    # Output: 'gajjela' (third element)
print(I[-1])   # Output: 'reddy' (last element)
print(I[-3])   # Output: 'gajjela' (third last element)

# 3.2 Using Slicing
I = ['raju','hampy','gajjela','viya','reddy']
print(I[1:4])  # Output: ['hampy', 'gajjela', 'viya'] (elements from index 1 to 3)
print(I[:3])   # Output: ['raju', 'hampy', 'gajjela'] (first three elements)
print(I[2:])   # Output: ['gajjela', 'viya', 'reddy'] (elements from index 2 to end)
print(I[-4:-1]) # Output: ['hampy', 'gajjela', 'viya'] (elements from index -4 to -2)   
print(I[:])    # Output: ['raju', 'hampy', 'gajjela', 'viya', 'reddy'] (entire list)
print(I[-3:])  # Output: ['gajjela', 'viya', 'reddy'] (last three elements)
print(I[:-2])  # Output: ['raju', 'hampy', 'gajjela'] (all elements except last two)
print(I[-5:-2]) # Output: ['raju', 'hampy', 'gajjela'] (elements from index -5 to -3)
print(I[::-1])  # Output: ['reddy', 'viya', 'gajjela', 'hampy', 'raju'] (reversed list)
print(I[-1:-6:-1]) # Output: ['reddy', 'viya', 'gajjela', 'hampy', 'raju'] (reversed list using negative indices)
print(I[-1:-6:-2]) # Output: ['reddy', 'gajjela', 'raju'] (every second element in reversed list)
print(I[::2])   # Output: ['raju', 'gajjela', 'reddy'] (every second element)
print(I[1::2])  # Output: ['hampy', 'viya'] (every second element starting from index 1)
print(I[::3])   # Output: ['raju', 'viya'] (every third element)
print(I[1:5:2]) # Output: ['hampy', 'viya'] (elements from index 1 to 4 with step 2)
print(I[-5:-1:2]) # Output: ['raju', 'gajjela'] (elements from index -5 to -2 with step 2)
print(I[-1:-6:-2]) # Output: ['reddy', 'gajjela', 'raju'] (elements from index -1 to -5 with step -2)
print(I[-2::-1]) # Output: ['viya', 'gajjela', 'hampy', 'raju'] (elements from index -2 to start in reverse order)
print(I[-1:0:-1]) # Output: ['reddy', 'viya', 'gajjela', 'hampy'] (elements from index -1 to 1 in reverse order)
print(I[3:0:-1]) # Output: ['viya', 'gajjela', 'hampy'] (elements from index 3 to 1 in reverse order)
print(I[4:1:-1]) # Output: ['reddy', 'viya', 'gajjela'] (elements from index 4 to 2 in reverse order)
print(I[::])    # Output: ['raju', 'hampy', 'gajjela', 'viya', 'reddy'] (entire list)
print(I[::-2])  # Output: ['reddy', 'gajjela', 'raju'] (every second element in reversed list)
print(I[1::-1]) # Output: ['hampy', 'raju'] (elements from index 1 to 0 in reverse order)
print(I[-3:2:-1]) # Output: ['gajjela', 'hampy'] (elements from index -3 to 3 in reverse order)
print(I[2::-1]) # Output: ['gajjela', 'hampy', 'raju'] (elements from index 2 to 0 in reverse order)
print(I[-4:1:-1]) # Output: ['hampy'] (elements from index -4 to 2 in reverse order)

# 4. Modifying Lists
# 4.1 Changing Elements & updating Values
M = ['raju','hampy','gajjela','viya','reddy']
M[2] = 'kumar'  # Changing the third element
print(M)  # Output: ['raju', 'hampy', 'kumar', 'viya', 'reddy']

# 4.2 Adding Elements(append, insert, extend)
A = ['raju','hampy','gajjela','viya','reddy']
A.append('srinu') # Adding an element at the end
print(A)  # Output: ['raju', 'hampy', 'gajjela', 'viya', 'reddy', 'srinu']
A.insert(4, 'akshitha') # Inserting an element at index 4
print(A)  # Output: ['raju', 'hampy', 'gajjela', 'viya', 'akshitha', 'reddy', 'srinu']
A.extend(['naveen','tapaswi']) # Extending the list with another list
print(A)  # Output: ['raju', 'hampy', 'gajjela', 'viya', 'akshitha', 'reddy', 'srinu', 'naveen', 'tapaswi']

# 4.3 Removing Elements
R = ['raju','hampy','gajjela','viya','reddy','hampy']
R.remove('hampy')  # Removing the first occurrence of 'hampy')
print(R)  # Output: ['raju', 'gajjela', 'viya', 'reddy', 'hampy']
R.pop(2) # Removing the element at index 2
print(R)  # Output: ['raju', 'gajjela', 'reddy', 'hampy']
R.pop()  # Removing the last element
print(R)  # Output: ['raju', 'gajjela', 'reddy']
del R[0]  # Deleting the element at index 0
print(R)  # Output: ['gajjela', 'reddy']
R.clear()  # Clearing the entire list
print(R)  # Output: []

# 5. index() & count()
IC = ['raju','viya','hampy','viya','gajjela','viya','reddy','hampy']
print(IC.index('gajjela')) # Output: 4 (index of first occurrence of 'gajjela')
print(IC.count('viya')) # Output: 3
print(IC.count('hampy')) # Output: 2

# 6. Sorting and Reversing Lists
a=[5,2,4,1,3]
a.sort()
print(a) # [1, 2, 3, 4, 5]
b = sorted(a)
print(b) # [1, 2, 3, 4, 5]
a.sort(reverse=True)
print(a) # [5, 4, 3, 2, 1]

r=["c","c++","python","java"]
r.reverse()
print(r) # ['java', 'python', 'c++', 'c']

# 7. Copying a List
# 7.1 Shallow Copy
y = [3,2,4,6,5]
c = y.copy()
print(c) # [3, 2, 4, 6, 5]
y.append(100)
print(y) # [3, 2, 4, 6, 5, 100]
print(c) # [3, 2, 4, 6, 5]

# 7.2 Deep copy
x = [1,2,3,4,5]
d = x
print(d) # [1, 2, 3, 4, 5]
x.append(500)
print(x) # [1, 2, 3, 4, 5, 500]
print(d) # [1, 2, 3, 4, 5, 500]

# 8. max(lst) & min(lst)
m = [1,5,10,15,20]
m1 = max(m)
print(m1) # 20
m2 = min(m)
print(m2) # 1

# 9. sum(lst) & len(lst)
sum_lst = [22,18,10]
s = sum(sum_lst)
print(s) # 50
len_lst = len(sum_lst)
print(len_lst) # 3

# 10. any(lst) & all(lst)
a = [0,0.0,'',(),False]
a1 = any(a)
print(a1)  # False
a2 = all(a) #False

b = [1,0.0,'',(),True]
b1 = any(b)
print(b1)  # True

c = [1,1.2,'all',(1,2,3),True]
c1 = all(c)
print(c1)  # # True