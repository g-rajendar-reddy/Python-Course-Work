
# 1. Common Exceptions:
#    ZeroDivisionError: Division by zero.
#    ValueError: Invalid value.
#    TypeError: Incompatible data types.
#    IndexError: Accessing an invalid index in a list.
#    KeyError: Accessing a non-existent key in a dictionary.
#    FileNotFoundError: File does not exist.

# 2. Basic Exception Handling
try:
    result = 10/0
except ZeroDivisionError:
    print("cannot divide by zero!")   
     
# 3. Multiple Except Blocks    
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")    

# 4. Catching Multiple Exceptions Together    
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")  

# 5. The else Clause
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful!", result)

# 6. The finally Clause
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
    file.close()    

# 7. Raising Exceptions
value = -10
if value < 0:
    raise ValueError("Value cannot be negative.")

# Custom Error Messages:
try:
    result = 10/0
except Exception as e:
    print(f"Error occured: {e}")   

# 8. Custom Exceptions
class NegativeValueError(Exception):
    pass
value = -5
if value < 0:
    raise NegativeValueError("Negative values are not allowed.")    

# 9. Nested Exception Handling
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Handled division by zero inside nested try block.")
except Exception as e:
    print(f"Outer exception handler: {e}")