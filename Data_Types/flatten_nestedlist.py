"""
Flatten a nested list (Advanced List Problem)

Convert a nested list into a single list.

👉 Input:

[1, [2, 3], [4, [5, 6]], 7]

"""
def flat(lst):
    new_list = []
    for d in lst:
        if isinstance(d, list):        #is instance checks if the data type matches to given
            new_list.extend(flat(d))   #recursion
        else:
            new_list.append(d)
    return new_list

lst = [1, [2, 3], [4, [5, 6]], 7]
print(flat(lst)) 