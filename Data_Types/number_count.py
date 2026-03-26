"""
Dictionary + List combination

Count how many numbers are in this structure:

data = {"nums": [1, 2, 3, 4, 5]}
"""
data = {"nums": [1, 2, 3, 4, 5,6,7,11,3,8,7,2,3,46,7,8,9]}

print(len(data['nums']))

#or

for d in data.values():
    count = 0
    for n in d:
        count+=1
    print(count)
    
#or 
data_count = len([n for d in data.values() for n in d])
print(data_count)