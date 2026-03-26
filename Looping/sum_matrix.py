#sum only even numbers of given matrix

def sum_of_evens(matrix):
    sum=0
    for i in matrix:
        
        for m in i:
            if m%2==0:
                sum+=m
    return sum
    
print(sum_of_evens([[1,2,3],[4,5,6],[7,8,9]]))