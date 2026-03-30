#Find common non-repetitive elements from both sets

def common_el(a,b):
    return a & b

print(common_el({2,5,6,8,9},{2,5,8,8,7,4,3}))

#or

def common_el(a,b):
    return a.intersection(b)

print(common_el({2,5,6,8,9},{2,5,8,8,7,4,3}))