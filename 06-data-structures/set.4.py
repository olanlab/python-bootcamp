set1 = {"mini cooper", "honda", "toyota"}
set2 = {"honda", "ford", "lexus"}

# difference
print(set1.difference(set2))
print(set2.difference(set1))

# intersection
print(set1.intersection(set2))
print(set2.intersection(set1))

# union
print(set1.union(set2))
print(set2.union(set1))

# subset
print(set1.issubset(set2))

# superset
print(set1.issuperset(set2))

# disjoint
print(set1.isdisjoint(set2))
