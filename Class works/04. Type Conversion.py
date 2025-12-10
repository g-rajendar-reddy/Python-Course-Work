# 1. Converting from int
int_a = 42
float(int_a)  # Converts to float: 42.0
str(int_a)    # Converts to string: '42'
bool(int_a)   # Converts to boolean: True (non-zero integers are True)
# list(int_a) # TypeError: 'int' object is not iterable
# tuple(int_a)  # TypeError: 'int' object is not iterable
# set(int_a)    # TypeError: 'int' object is not iterable
# dict(int_a)   # Raises TypeError: int object is not iterable

# 2. Converting from float
float_b = 3.14
int(float_b)  # Converts to int: 3 (truncates decimal part)
str(float_b)    # Converts to string: '3.14'
bool(float_b)   # Converts to boolean: True (non-zero floats are True)
# list(float_b) # TypeError: 'float' object is not iterable
# tuple(float_b)  # TypeError: 'float' object is not iterable
# set(float_b)    # TypeError: 'float' object is not iterable
# dict(float_b)   # Raises TypeError: float object is not iterable

# 3. Converting from string
str_c = "123"
int(str_c)    # Converts to int: 123 (if string is numeric)
# int("123.45")  # Raises ValueError: invalid literal for int() with base 10: '123.45'
# int("abc")    # Raises ValueError: invalid literal for int() with base 10: 'abc'
float(str_c)  # Converts to float: 123.0 (if string is numeric
float("123.45")  # Converts to float: 123.45
# float("abc")  # Raises ValueError: could not convert string to float: 'abc'
bool(str_c)   # Converts to boolean: True (non-empty strings are True)
list(str_c)   # Converts to list: ['1', '2', '3']
tuple(str_c)  # Converts to tuple: ('1', '2', '3')
set(str_c)    # Converts to set: {'1', '2', '3'} (unique characters)
# dict(str_c)   # Raises ValueError: dictionary update sequence element #0 has length 1; 2 is required

# 4. List conversion
list_d = [1, 2, 3]
# int(list_d)    # Raises TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# float(list_d)  # Raises TypeError: float() argument must be a string or a number, not 'list'
str(list_d)    # Converts to string: '[1, 2, 3]'
bool(list_d)   # Converts to boolean: True (non-empty lists are True)
tuple(list_d)  # Converts to tuple: (1, 2, 3)
set(list_d)    # Converts to set: {1, 2, 3}
# dict(list_d)   # Raises TypeError: cannot convert dictionary update sequence element #0

# 5. Tuple conversion
tuple_e = (4, 5, 6)
# int(tuple_e)    # Raises TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
# float(tuple_e)  # Raises TypeError: float() argument must be a string or
str(tuple_e)    # Converts to string: '(4, 5, 6)'
bool(tuple_e)   # Converts to boolean: True (non-empty tuples are True)
list(tuple_e)   # Converts to list: [4, 5, 6]
set(tuple_e)    # Converts to set: {4, 5, 6}
# dict(tuple_e)   # Raises TypeError: cannot convert dictionary update sequence element #0

# 6. Set conversion
set_f = {7, 8, 9}
# int(set_f)    # Raises TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
# float(set_f)  # Raises TypeError: float() argument must be a string or
str(set_f)    # Converts to string: '{8, 9, 7}' (order may vary)
bool(set_f)   # Converts to boolean: True (non-empty sets are True)
list(set_f)   # Converts to list: [8, 9, 7] (order may vary)
tuple(set_f)  # Converts to tuple: (8, 9, 7)
# dict(set_f)   # Raises TypeError: cannot convert dictionary update sequence element #0

# 7. Dictionary conversion
dict_g = {'a': 1, 'b': 2}
# int(dict_g)    # Raises TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
# float(dict_g)  # Raises TypeError: float() argument must be a string or
str(dict_g)    # Converts to string: "{'a': 1, 'b': 2}"
bool(dict_g)   # Converts to boolean: True (non-empty dictionaries are True)
list(dict_g)   # Converts to list: ['a', 'b'] (list of keys)
tuple(dict_g)  # Converts to tuple: ('a', 'b') (tuple of keys)
set(dict_g)    # Converts to set: {'a', 'b'} (set of

# 8. Boolean conversion
bool_g = True
int(bool_g)    # Converts to int: 1
float(bool_g)  # Converts to float: 1.0
str(bool_g)    # Converts to string: 'True'
# list(bool_g)   # Error not iterable
# tuple(bool_g)  # Error not iterable
# set(bool_g)    # Error not iterable
# dict(bool_g)   # Raises TypeError: cannot convert dictionary update sequence element #0

# 9. Dictionary Conversion
d = [
    ('Name', 'Rajendar'),
    ('Age', '24'),
    ('Education', 'B.Tech'),
    ('Birthplace', 'Shadnagar')
]
cd = dict(d)  # Converts list of tuples to dictionary)
print(cd) # output: {'Name': 'Rajendar', 'Age': '24', 'Education': 'B.Tech', 'Birthplace': 'Shadnagar'}

