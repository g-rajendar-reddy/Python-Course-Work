from datetime import date,time, datetime, timedelta

today = date.today()
print(today)                # Output : 2026-01-08
print(today.year)           # Output : 2026
print(today.month)          # Output : 1
print(today.day)            # Output : 8
print(today.weekday())      # Output : 3
print(today.isoweekday())   # Output : 4


today = date(2000,5,31)
print(today)              # Output: 2000-05-31

today=time(5,30,50)
print(today)              # Output: 05:30:50


now = datetime.now()
print(now)                      # Output: 2026-01-08 20:34:29.226457
print("Year:",now.year)         # Output: Year: 2026
print("Month:", now.month)      # Output: Month: 1
print("Day:", now.day)          # Output: Day: 8
print("Hour:", now.hour)        # Output: Hour: 20
print("Minute:", now.minute)    # Output: Minute: 34
print("Second:",now.second)     # Output: Second: 29


now = datetime.now()
print(now)                                          # Output: 2026-01-08 20:39:49.710170
print(now.strftime('%d/%m/%Y'))                     # Output: 08/01/2026
print(now.strftime('%H:%M:%S'))                     # Output: 20:39:49
print(now.strftime('%I:%M:%S'))                     # Output: 08:39:49
print(now.strftime('%A,%d %b %y %I:%M:%S %p'))      # Output: Thursday,08 Jan 26 08:39:49 PM


today = date.today()
n = today + timedelta(days=5)
print(n)        # Output: 2026-01-13

now = datetime.now()
h = now - timedelta(hours=2)
print(h)        # Output: 2026-01-08 18:41:54.597524


import sys

print(sys.argv)
print(sys.path)
print(sys.version)

print("start")
sys.exit()
print("End")
# Output: Start


import platform

print(platform.system())        # Output: Windows
print(platform.release())       # Output: 11
print(platform.processor())     # Output: Intel64 Family 6 Model 154 Stepping 4, GenuineIntel


import math

print(math.pi)              # Output: 3.141592653589793
print(math.e)               # Output: 2.718281828459045
print(math.sqrt(64))        # Output: 8.0
print(math.pow(2,4))        # Output: 16.0
print(round(12.3))          # Output: 12
print(math.ceil(12.8))      # Output: 13
print(math.floor(12.8))     # Output: 12
print(math.gcd(12,24))      # Output: 12




from collections import Counter, defaultdict, deque

n = 'My name is Rajendar Reddy. I am from shadnagar'
display = Counter(n)
print(display)
# Output: Counter({' ': 8, 'a': 7, 'd': 4, 'n': 3, 'm': 3, 'e': 3, 'r': 3, 'y': 2, 's': 2, 'R': 2, 'M': 1, 'i': 1, 'j': 1, '.': 1, 'I': 1, 'f': 1, 'o': 1, 'h': 1, 'g': 1})


from collections import defaultdict

count = defaultdict(int)

count["apple"] += 1
count["banana"] += 2

print(count) # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})


q = deque([])
q1=q.appendleft(1)
q2=q.append(3)
q3=q.append(5)
q4=q.pop(3)
q4=q.popleft(1)
print(q,q1,q2,q3,q4)