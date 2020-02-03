from collections import Counter

c = Counter("string repreast")
for key in c.keys():
  if c[key]>=2:
    break
    
print(key) 
