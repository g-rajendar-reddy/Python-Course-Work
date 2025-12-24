'''
Q1. Even or Odd Checker (if–else)
Write a program that takes an integer as input and checks whether the number is even or
odd.
Input:
An integer number
Output:
Print "Even Number" if the number is even, otherwise print "Odd Number".
Sample Input:
12
Sample Output:
Even Number
'''
a = int(input())
if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print('-'*30)

'''
Q2. Positive, Negative or Zero (if–elif–else)
Write a program that reads a number and prints whether it is Positive, Negative or Zero.
Input:
An integer number
Output:
Print "Positive Number", "Negative Number" or "Zero".
Sample Input:
0
Sample Output:
Zero
'''
b = int(input())
if b > 0:
    print("Positive Number")
elif b < 0:
    print("Negative Number")    
else:
    print("Zero")

print('-'*30)

'''
Q3. Voting Eligibility Check (simple if)
A person is eligible to vote only if their age is 18 or above.
Write a program that takes age as input and prints "Eligible to Vote" only if the condition is
satisfied.

Input:
Age (integer)
Output:
Eligible to Vote
Sample Input:
20
Sample Output:
Eligible to Vote
'''
age = int(input())
if age >= 18:
    print("Eligible to Vote")

print('-'*30)

'''
Q4. Largest of Two Numbers (if–else)
Write a program to find the largest of two numbers.
Input:
Two integers (one per line)
Output:
Print the larger number.
Sample Input:
10
20
Sample Output:
20
'''
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(num1)
else:
    print(num2)

print('-'*30)

'''
Q5. Largest of Three Numbers (nested if)
Write a program to find the largest of three numbers using nested if statements.
Input:
Three integers (one per line)
Output:
Print the largest number.
Sample Input:
10
25
15
Sample Output:
25
'''
num1 = int(input())
num2 = int(input()) 
num3 = int(input())
if num1 >= num2:
    if num1 >= num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 >= num3:
        print(num2)
    else:
        print(num3)

print('-'*30)

'''     
Q6. Grade Calculator (if–elif–else)
Write a program that prints the grade based on the marks given below:
Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Marks < 50 → Fail
Input:
Marks (integer)
Output:
Grade or Fail
Sample Input:
82
Sample Output:
B
'''
marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print('-'*30)

''' 
Q7. Login Validation (nested if)
The stored username is "admin" and password is "1234".
Write a program that takes username and password as input and validates login.
Input:
Username
Password
Output:
Print "Login Successful" if both are correct.
Print "Wrong Password" if username is correct but password is wrong.
Print "Invalid Username" if username is incorrect.
Sample Input:
admin
1234
Sample Output:
Login Successful
'''

stored_username = "admin"
stored_password = "1234"
input_username = input()
input_password = input()
if input_username == stored_username:
    if input_password == stored_password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

print('-'*30)

'''
Q8. Number Range Checker (if–elif–else)
Write a program to check whether a number lies in the following ranges:
1 to 10
11 to 20
Greater than 20

Input:
An integer number
Output:
Print the range in which the number belongs.
Sample Input:
15
Sample Output:
Between 11 and 20
'''
num = int(input())
if 1 <= num <= 10:
    print("Between 1 and 10")
elif 11 <= num <= 20:
    print("Between 11 and 20")
else:
    print("Greater than 20")

print('-'*30)

'''
Q9. Simple Calculator (if–elif–else)
Write a program that performs arithmetic operations based on user choice.
Input:
First number
Second number
Operator (+, -, *, /)
Output:
Print the result of the operation.
Sample Input:
10
5
+
Sample Output:
15
'''
num1 = float(input())
num2 = float(input())
operator = input()
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid Operator")

print('-'*30)

'''
Q10. Pass or Fail Checker (if–else)
A student passes the exam if marks are 40 or above.
Write a program to check whether the student has passed or failed.
Input:
Marks (integer)
Output:
Print "Pass" or "Fail".
Sample Input:
38
Sample Output:
Fail
'''
marks = int(input())
if marks >= 40:
    print("Pass")
else:
    print("Fail")

'''
All Outputs
3
Odd Number
------------------------------
-4
Negative Number
------------------------------
24
Eligible to Vote
------------------------------
35
75
75
------------------------------
25
83
37
83
------------------------------
85
Grade B
------------------------------
Raju
12345
Invalid Username
------------------------------
25
Greater than 20
------------------------------
3.4
5.2
+
8.6
------------------------------
35
Fail
'''