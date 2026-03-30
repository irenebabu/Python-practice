#find symmetric difference between two sets
def symm_diff(a,b):
    
    print(a.symmetric_difference(b))   

symm_diff({1,2,3,4},{3,4,5,6})

#or

def symmetric_difference(set1, set2):
    return set1 ^ set2 

print(symmetric_difference({1,2,3,4},{3,4,5,6}))
