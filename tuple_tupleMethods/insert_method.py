#create a new tuple containing only the values belonging to the indices of the given list

def copy_elements(original_tuple, indices):
    return tuple(original_tuple[i] for i in indices)


print(copy_elements((1,2,3,4,5,6,7),[0,1,4]))