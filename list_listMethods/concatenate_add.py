#concatenate two lists and add the second and second last element

def con_add(l1,l2):
    final_list = l1 + l2
    result = final_list[1] + final_list[-2]
    return final_list,result

print(con_add([6,5,4,1],[2,5,4,7]))

