def diff(a,b):
    return a.difference(b)

print(diff({5,6,7,2,1,3,5,6,9,8},{5,6,7,2,1,3}))

#or

def diff(a,b):
    return a - b

print(diff({5,6,7,2,1,3,5,6,9,8},{5,6,7,2,1,3}))