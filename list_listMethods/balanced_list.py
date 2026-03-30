#check if list is balanced or not , sum of first half of elements = second half  (use slicing)

def is_balanced(lst):
    if len(lst)%2!= 0:
        return False   
    mid = len(lst) // 2
    return sum(lst[:mid]) == sum(lst[mid:])
        
print(is_balanced([1,2,3,3,2,1]))
print(is_balanced([6,2,3,3,2,1]))