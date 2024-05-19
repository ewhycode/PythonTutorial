#SETS: duplicate values not allowed and order does not matter
#data collection
#sets mimics mathematical sets
#declared using curly brackets {}

set1 = {5}
print(type(set1))
set1 = {5,6,5,5,5,5,5,5,5,5,5}
print(type(set1))
print(set1)
set2 = {2,3,4,5,5,3}

#UNION: add 2sets of values

print(set1.union(set2))

print('intersection')
print(set1.intersection(set2))
print(set1 & set2)

print('difference')
print(set1.difference(set2))
print(set1-set2)
print(set2.difference(set1))