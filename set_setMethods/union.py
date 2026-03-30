#Combine both sets and remove duplicates

def union_sets(a,b):
    return a | b

print(union_sets({1,2,3},{3,4,5}))

#or

def union_sets(a,b):
    return a.union(b)
print(union_sets({1,2,3},{3,4,5}))

