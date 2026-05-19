
# Match
import re
pattern = r'[0-9]'
res = re.match(pattern,"12hajJWH")
print(res.group() if res else "Match not found")
#Output: 1

# Search
import re
pattern = r'[aeiou]'
res = re.search(pattern,"hello")
print(res.group() if res else "Match not found")

# Find all
import re
pattern = r'[aeiou]'
res = re.findall(pattern,"hello")
print(res)
#Output: ['e', 'o'] 

# finditer
import re
pattern = r'[aeiou]'
res = re.finditer(pattern,"hello")

for i in res:
    print(i.group(),i.start())

#Output: e 1
#        o 4    

# Split
import re
pattern = r'[@*=&.,]'
res = re.split(pattern,"h@e*l=l&o.e,s")
print(res)
#Output: ['h', 'e', 'l', 'l', 'o', 'e', 's']

# Sub
import re
pattern = r'[aeiou]'
res = re.sub(pattern,"*","hello")
print(res)
# Output: h*ll*
