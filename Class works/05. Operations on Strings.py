# 1. Concatenation
str1 = "Hello, "
str2 = "World!"
result_concat = str1 + str2
print("Concatenation:", result_concat)  # Output: Hello, World!

# 2. Repetition
str3 = "Ha"
result_repeat = str3 * 3
print("Repetition:", result_repeat)  # Output: HaHaHa

# 3. Indexing
str4 = "Python"
first_char = str4[0]
last_char = str4[-1]
print("First character:", first_char)  # Output: P
print("Last character:", last_char)    # Output: n

# 4. Slicing
str5 = "Programming"
slice_substring = str5[0:6]  # 'Progra'
print("Sliced substring:", slice_substring)  # Output: Progra
# Slicing with step
step_slice = str5[0:10:2]  # 'Prgam'
print("Sliced with step:", step_slice)  # Output: Prgam
# Slicing with negative step
neg_step_slice = str5[10:0:-1]  # 'gnimmarg
print("Sliced with negative step:", neg_step_slice)  # Output: gnimmarg
# Slicing to reverse a string
reversed_str = str5[::-1]  # 'gnimmargorP'
print("Reversed string:", reversed_str)  # Output: gnimmargorP

# 5. String Membership
sample_str = "Hello, Python!"
is_in = "Python" in sample_str
is_not_in = "Java" not in sample_str
print("'Python' in string:", is_in)        # Output: True
print("'Java' not in string:", is_not_in)  # Output: True

# 6. String Methods
str6 = "  hello world  "
upper_str = str6.upper()
lower_str = str6.lower()
capitalize_str = str6.capitalize()
title_str = str6.title()
swapcase_str = str6.swapcase()
casefold_str = "groß".casefold()

print("Uppercase:", upper_str)          # Output:   HELLO WORLD  
print("Lowercase:", lower_str)          # Output:   hello world
print("Capitalized:", capitalize_str)   # Output:   Hello world
print("Title Case:", title_str)         # Output:   Hello World
print("Swap Case:", swapcase_str)       # Output:   HELLO WORLD
print("Casefolded 'groß':", casefold_str)  # Output: gross

# 6. String Alignment & Formatting Methods
Name = "Rajendar"
s1 = Name.center(20, '*') # ******Rajendar******
s2 = Name.ljust(20, '-')  # Rajendar----------
s3 = Name.rjust(20, '+')  # ++++++++++Rajendar
s4 = Name.zfill(20)       # 0000000000Rajendar
print(s1, s2, s3, s4, sep="\n")

# 7. String Search & Find Methods
str7 = "Welcome to the world of Python programming. Python is fun!"
F1=str7.find("o") # output: 4
F2=str7.rfind("o") # output: 48
F3=str7.find("Z") # output: -1
I1=str7.index("o") # output: 4
I2=str7.rindex("o") # output: 48
# I3=str7.index("Z") # Raises ValueError
C1=str7.count("o") # output: 7
# C2=str7.count() # output: TypeError: count() takes at least 1 argument (0 given)
print(F1,F2,F3,I1,I2,C1,sep="\n") 

# 8. String Replace & Modify Methods
str8 = "I love Python. Python is great for data science."
R1 = str8.replace('data science', 'AI and ML') # Replaces 'data science' with 'AI and ML'
R2 = str8.replace('java','c++') # No change as 'java' not found
print(R1,R2)

T1 = str8.translate(str.maketrans('abc','*+#')) # Replaces 'a' with '*', 'b' with '+', 'c' with '#'
print(T1) # output: I love Python. Python is gre*t for d#t* s#ien#e.
T2 = str8.maketrans('abc','*+#')
print(T2) # output : {97: 42, 98: 43, 99: 35}

# 9. String len(),ord(),chr(),min(),max() & sorted() Methods
str9 = "Rajendar Reddy"
L = len(str9) # output: 14
O = ord('R') # output: 82
# emoji = chr(128579) # output: '😃'
min_char = min(str9) # output: ' '
max_char = max(str9) # output: 'y'
sorted_str = sorted(str9) # output: [' ', 'R', 'a', 'a', 'd', 'd', 'e', 'e', 'j', 'n', 'r', 'r', 'y']
sorted_str1 = sorted(str9,reverse=True) # output: ['y', 'r', 'r', 'n', 'j', 'e', 'e', 'd', 'd', 'a', 'a', 'R', ' ']
print(L,O,min_char,max_char,sorted_str,sorted_str1,sep="\n")

# 10. String Split & Join Methods
S = "Rajendar Reddy Gajjela"
s1 = S.split() # Default split by whitespace
s2 = S.split('e') # Split by character 'e'
s3 = S.split(' ', 1) # Split by whitespace, max 1 split
s4 = S.rsplit(' ', 1) # Right split by whitespace, max 1 split
print(s1) # output: ['Rajendar', 'Reddy', 'Gajjela']
print(s2) # output: ['Raj', 'ndar R', 'ddy Gajj', 'la']
print(s3) # output: ['Rajendar', 'Reddy Gajjela']
print(s4) # output: ['Rajendar Reddy', 'Gajjela']

sp = """good morning everyone
Have a nice day
all the best"""
sp1 = sp.splitlines() # Split at line breaks
print(sp1) # output: ['good morning  everyone', 'Have a nice day', 'all the best ']    
J1 = '_'.join(S) # Join with '-'
print(J1) # output: R_a_j_e_n_d_a_r_ _R_e_d_d_y_ _G_a_j_j_e_l_a

P = "1.python_demo.py"
p1 = P.partition('.') # Partitions at first '.'
p2 = P.rpartition('.') # Partitions at last '.'
print(p1) # output: ('1', '.', 'python_demo.py')
print(p2) # output: ('1.python_demo', '.', 'py')

# 11. String Whitespace Removal & Trimming Methods
wr = "   Hello, World!   "
wr1 = wr.strip()  # Removes leading and trailing whitespace
wr2 = wr.lstrip() # Removes leading whitespace
wr3 = wr.rstrip() # Removes trailing whitespace
print(wr1) # Output: "Hello, World!"
print(wr2) # Output: "Hello, World!   "
print(wr3) # Output: "   Hello, World!"

# 12. Encoding & Decoding
Name = "Rajendar Reddy"
encoded_name = Name.encode()  # Encode to bytes
decoded_name = encoded_name.decode()  # Decode back to string
print("Encoded:", encoded_name)  # Output: b'Rajendar Reddy'
print("Decoded:", decoded_name)  # Output: Rajendar Reddy

# 13. String Testing Methods (Boolean Results)
ts = "Hello123"
ts1 = ts.isalpha()       # False, contains digits      
ts2 = ts.isdigit()       # False, contains letters
ts3 = ts.isalnum()       # True, contains only letters and digits
ts4 = ts.islower()       # False, contains uppercase letters
ts5 = ts.isupper()       # False, contains lowercase letters
ts6 = ts.isspace()       # False, contains non-space characters
ts7 = ts.istitle()       # True, each word starts with uppercase
ts8 = ts.startswith("He")  # True
ts9 = ts.endswith("23")    # True
ts10 = "   ".isspace()    # True, only spaces
ts11 = ts.isidentifier() # True, valid identifier
ts12 = ts.isdecimal()   # False, contains letters
ts13 = ts.isnumeric()   # False, contains letters
ts14 = ts.isdigit()     # False, contains letters
print(ts1, ts2, ts3, ts4, ts5, ts6, ts7, ts8, ts9, ts10, ts11, ts12, ts13, ts14, sep="\n")