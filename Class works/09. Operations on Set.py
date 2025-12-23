# 1. Introduction to Sets
# ● A set is an unordered, mutable collection of unique elements.
# ● Sets automatically remove duplicate elements.
# ● Sets are similar to mathematical sets and support operations like union, intersection, and difference.
# ● They are useful for storing unique elements and performing fast membership tests.

# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Set is an unordered
unordered = {18,93,23,32,48,59}
print(unordered)  # Output : {32, 48, 18, 23, 59, 93}
# Creating an empty set (use set() function, not {})
empty_set = set()
# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output : {1, 2, 3, 4}

# 2. Set Properties
# ● Unordered: Sets do not maintain the insertion order.
# ● Unique Elements: Duplicate elements are not allowed.
# ● Mutable: Sets can be modified (elements can be added or removed).
# ● Immutable Elements Only: Elements must be hashable (mutable types like lists cannot be elements).
# Example of an invalid set (due to mutable elements):
# This will raise a TypeError
# invalid_set = {[1, 2], 3} # Lists are mutable and cannot be added to a set

# 3. Operations on Sets
# a. Membership Testing
x = {1,2,3,4,5}
print(1 in x)   # Output:True
print(1 not in x)   # Output:False

# b. Union (| or union() method)
# ● Combines elements from two sets (removes duplicates).
# ● Syntax: set1 | set2 or set1.union(set2)
a = {1,2,3}
b = {2,3,4}
c = a.union(b)
print(c)    # Output:{1, 2, 3, 4}

# c. Intersection (& or intersection() method)
# ● Returns common elements between two sets.
# ● Syntax: set1 & set2 or set1.intersection(set2)
a = {1,2,3}
b = {2,3,4}
c = a.intersection(b)
print(c)    # Output:{2, 3}

# d. Difference (- or difference() method)
# ● Returns elements in the first set but not in the second set.
# ● Syntax: set1 - set2 or set1.difference(set2)
a = {1,2,3}
b = {2,3,4}
c = a.difference(b)
print(c)    # Output:{1}

# e. Symmetric Difference (^ or symmetric_difference() method)
# ● Returns elements in either set1 or set2 but not both.
# ● Syntax: set1 ^ set2 or set1.symmetric_difference(set2)
a = {1,2,3}
b = {2,3,4}
c = a.symmetric_difference(b)
print(c)    # Output:{1, 4}

# f. Subset (<= or issubset() method)
# ● Checks if all elements of one set are present in another.
# ● Syntax: set1 <= set2 or set1.issubset(set2)
a = {2,3}
b = {2,3,4}
c = a.issubset(b)
print(c)    # Output:True

a = {2,6}
b = {2,3,4}
c = a.issubset(b)
print(c)    # Output:False

# g. Superset (>= or issuperset() method)
# ● Checks if one set contains all elements of another.
# ● Syntax: set1 >= set2 or set1.issuperset(set2)
a = {1,2,3}
b = {2,3}
c = a.issuperset(b)
print(c)    # Output:True

a = {1,2,3}
b = {3,4}
c = a.issuperset(b)
print(c)    # Output:False

# h. Disjoint Sets (isdisjoint() method)
# ● Returns True if two sets have no common elements.
a = {1,2,3}
b = {4,5,6}
c = a.isdisjoint(b)
print(c)    # Output:True

a = {1,2,3}
b = {3,5,6}
c = a.isdisjoint(b)
print(c)    # Output:False

# 4. Built-in Methods for Sets
s = {3,5,2,6}
s.add(100)
print(s)   # Output:{2, 3, 100, 5, 6}
s.remove(5)
print(s)   # Output:{2, 3, 100, 6}
s.discard(100)
print(s)    # Output:{2, 3, 6}
s.discard(500)
print(s)    # Output: handle the error
s.pop()
print(s)    # Output: {3, 6}
s.clear()  
print(s)    # Output: set()

# update
a={12,34,67}
b={32,65,23}
a.update(b)
print(a) # Output: {32, 65, 34, 67, 23, 12}

# shallow copy
a={12,34,67}
b = a.copy()
print(b) # Output: {34, 67, 12}
# Deep copy
c=b
print(c) # Output: {34, 67, 12}

# 5. Built-in Functions for Sets
a = {1,4,2,3,6,5}
l = len(a)
print(l)    # Output: 6
print(max(a))   # Output: 6
print(min(a))   # Output: 1
print(sorted(a))    # Output: [1, 2, 3, 4, 5, 6]

lst=[3,1,7,54,2,0]
c = set(lst)
print(c)    # Output: {0, 1, 2, 3, 7, 54}