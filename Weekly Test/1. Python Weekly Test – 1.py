# Topics: Strings, Lists, Tuples, Type Conversion, Operators
# Q1.
text = "Hello World"
# Convert the string to lowercase
t = text.lower()
print(t)  # output:hello world

# Q2.
greeting = "good morning"
# Convert the string to uppercase
g = greeting.upper()
print(g)  # output:GOOD MORNING

# Q3.
data = " python "
# Remove leading and trailing spaces
d = data.strip()
print(d)  # output:python

# Q4.
line = "Python is tough"
# Replace "tough" with "easy"
l = line.replace("tough","easy")
print(l)   # output:Python is easy

# Q5.
word = "banana"
# Count how many times "a" appears
w = word.count('a')
print(w)  # output:3

# Q6.
text = "python is fun"
# Split the string into a list of words
t1 = text.split()
print(t1)   # output:['python', 'is', 'fun']

# Q7.
sentence = "learn python"
# Find the length of the string
s = len(sentence)
print(s)   # output:12

# Q8.
value = "test123"
# Check whether the string is alphanumeric
v = value.isalnum()
print(v)  # output:True

# Q9.
text = "HELLO"
# Convert to lowercase and capitalize the first letter
t2 = text.lower()   # output:hello
c = t2.capitalize()
print(c)    # output:Hello

# Q10.
email = "student@domain.com"
# Check if the string ends with ".com"
e = email.endswith('.com')
print(e)    #output:True

# Q11.
numbers = [45, 67, 89, 32]
# Sort the list in ascending order
numbers.sort()
print(numbers)    #output: [32, 45, 67, 89]

# Q12.
nums = [10, 20, 30]
# Add 40 to the end of the list
nums.append(40)
print(nums)     #output:[10, 20, 30, 40]

# Q13.
colors = ["red", "blue", "green"]
# Remove "blue" from the list
colors.remove("blue")
print(colors)   #output:['red', 'green']

# Q14.
values = [1, 2, 3, 2, 1]
# Count how many times 2 appears
v = values.count(2)
print(v)    #output:2

# Q15.
items = ["pen", "book", "pencil"]
# Join items into a single string separated by commas
j = ','.join(items)
print(j)    #output:'pen,book,pencil'

# Q16.
scores = [100, 90, 80]
# Reverse the list
scores.reverse()
print(scores)   #output:[80, 90, 100]

# Q17.
students = ("Anu", "Ravi", "Meena")
# Get the second element
s = students[1]
print(s)    #output:Ravi

# Q18.
details = ("ID101", "Sita", "CSE")
# Convert the tuple into a list
c = list(details)
print(c)    #output:['ID101', 'Sita', 'CSE']

# Q19.
data = (5, 3, 9, 1)
# Find the maximum value
f = max(data)
print(f)    #output:9

# Q20.
group = ("A", "B", "C", "D")
# Get the last two elements using slicing
s = group[-2::]
print(s)    #output:('C', 'D')

# Q21.
a = "10"
b = "20"
# Convert both to integers and find the sum
c = int(a)+int(b)
print(c)    #output:30

# Q22.
num = 25
# Convert this number to a string
s = str(num)
print(s)    #output:'25'

# Q23.
x = 10
y = 3
# Find the remainder when x is divided by y
d = x%y
print(d)    #output:1

# Q24.
a = 5
b = 2
# Find a raised to the power b
b = a**b
print(b)    #output:25

# Q25.
p = 15
q = 20
# Check whether p is less than q
c = p<q
print(c)    #output:True

# Q26.
numbers = [1, 2, 3, 4, 5]
# Find the sum of all elements
f = sum(numbers)
print(f)    #output:15

# Q27.
data = [3, 7, 1, 9]
# Find the maximum element
f1 = max(data)
print(f1)   #output:9

# Q28.
word = "mississippi"
# Count the number of occurrences of "s"
c = word.count("s")
print(c)    #output:4

# Q29.
text = "I love Python"
# Replace "love" with "learn"
t5 = text.replace("love","learn")
print(t5)   #output:'I learn Python'

# Q30.
values = [10, 20, 30, 40]
# Convert this list into a tuple
c = tuple(values)
print(c)    #output:(10, 20, 30, 40)