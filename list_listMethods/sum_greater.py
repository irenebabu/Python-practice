#Calculate sum of numbers greater than given number

def sum_greater_than(numbers, n):
    sum = 0
    for i in numbers:
        if i>n:
            sum = sum + i
    return sum

print(sum_greater_than([1,2,3,4,5],3))