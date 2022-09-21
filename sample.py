from itertools import permutations

d=list(permutations('hA'))
print(d)

print('\n')
#combinations
from itertools import combinations
g=list(combinations('abc',2))
print(g)

#forzenset
d=frozenset({'apple','banana'})
print(d)

f=49
d=("{:.2f}".format(f))
print(d)


#to check prime number:
#1,2,3,5,7,11,13,17,19...
