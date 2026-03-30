#sort a tuple of tuples by second element of each

def sort_tuples(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    return sorted_tuples

print(sort_tuples((('a',3),('b',2),('c',1))))