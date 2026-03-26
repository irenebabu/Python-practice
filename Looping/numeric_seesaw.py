#display a list of numbers which creates a numeric seesaw.if n = 5; eg :[1,2,3,4,5,4,3,2,1]
def numeric_seesaw(n):
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    
    for s in range(n-1,0,-1):
        lst.append(s)
    return lst
print(numeric_seesaw(3))