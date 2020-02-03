from collections import Counter
given = "this be the given string"

c = Counter(given)

single = "".join([i for i in c.keys() if c[i] == 1])
mul = "".join([i for i in c.keys() if c[i] > 1])
