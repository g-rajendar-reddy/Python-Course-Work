
def f(a,b):
    return a+b
print(f(2,3))

f = lambda a,b : a+b
print(f(2,3))  # Output: 5


def fun(num):
    return num*num
print(fun(5))

fun = lambda num : num*num
print(fun(5)) # Output: 25



even_odd = lambda x: "even" if x%2==0 else "odd"
print(even_odd(8)) 

'''
m = lambda a,b: a "max" if a > b else b "min"
print(m(10))
'''