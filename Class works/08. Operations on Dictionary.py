# 1. Introduction to Dictionary
# A dictionary in Python is an ordered, mutable collection that stores key-value pairs.
# Unlike lists or tuples, which are indexed by position, dictionaries are indexed by unique keys.

# Syntax of a Dictionary:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

# Example of a Dictionary:
emp = {
    'empid' : 121,
    'empname' : 'raju',
    'empsalary' : 40000,
    'empaddress': 'hyd'
}
print(emp)
# Output : {'empid': 121, 'empname': 'raju', 'empsalary': 40000, 'empaddress': 'hyd'}

# 2. Dictionary Operations
# 2.1 Accessing Values
print(emp['empname'])   #Output:raju
# print(emp["emprole"])   # KeyError
print(emp.get("empsalary"))     #Output:40000
print(emp.get("emprole"))   #Output:None it's handle error

# 2.2 Adding and Updating Items
emp["empid"] = 100
print(emp)
# Output : {'empid': 100, 'empname': 'raju', 'empsalary': 40000, 'empaddress': 'hyd'}

emp["emprole"] = 'PFD'
print(emp)
# Output : {'empid': 100, 'empname': 'raju', 'empsalary': 40000, 'empaddress': 'hyd', 'emprole': 'PFD'}

# 2.3 Removing Items from a Dictionary
rm = emp.pop("emprole")
print(rm)  # PFD
print(emp)   # Output : {'empid': 100, 'empname': 'raju', 'empsalary': 40000, 'empaddress': 'hyd'}
del emp["empsalary"]
print(emp)   # Output : {'empid': 100, 'empname': 'raju', 'empaddress': 'hyd'}
emp.popitem()
print(emp)     # Output : {'empid': 100, 'empname': 'raju'}
emp.clear()
print(emp)     # Output : {}

# 3. Dictionary Built-in Methods
# 3.1 Dictionary Methods for Accessing Data
emp = {
    'empid' : 121,
    'empname' : 'raju',
    'empsalary' : 40000,
    'empaddress': 'hyd'
}
print(emp.keys())   # Output : dict_keys(['empid', 'empname', 'empsalary', 'empaddress'])
print(emp.values())    # Output : dict_values([121, 'raju', 40000, 'hyd'])
print(emp.items())    # Output : dict_items([('empid', 121), ('empname', 'raju'), ('empsalary', 40000), ('empaddress', 'hyd')])

# 3.2 Dictionary Methods for Adding and Updating Data
emp.update({'emprole':'python','empsno':1})
print(emp)
# Output : {'empid': 121, 'empname': 'raju', 'empsalary': 40000, 'empaddress': 'hyd', 'emprole': 'python', 'empsno': 1}

# 4. Built-in Functions for Dictionaries
data = {'k1':'v1','k2':'v2','k3':'v3'}
print(len(data))    # Output : 3
print(min(data))    # Output : k1
print(max(data))    # Output : k3
print(sorted(data)) # Output :  ['k1', 'k2', 'k3']

# 5. Nested Dictionaries
students = {
"Raju": {"age": 24, "course": "python"},
"Kotesh": {"age": 25, "course": "java"}
}
print(students['Raju']['course'])  # Output : python