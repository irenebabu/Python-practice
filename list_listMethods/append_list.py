#write a function to repeat the same item multiple times in a list

def repeat_item(item, n):
    lst = []
    result = item*n
    for i in result:
        lst.append(i)
    return lst

print(repeat_item('a',3))


