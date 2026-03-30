#find sum of smallest two numbers in list without sort()

def sum_of_smallest(numbers):
    smallest = min(numbers)
    numbers.remove(smallest)
    second_smallest = min(numbers)
    
    print(smallest + second_smallest)

sum_of_smallest([7,5,6,8,3])

 #or

def sum_of_smallest(numbers):
    
    smallest = min(numbers)
    second_smallest = float('inf')
        
    for i in numbers:
        if i!=smallest and i<second_smallest:
            second_smallest = i
    total = smallest + second_smallest

    print(total)

sum_of_smallest([7,5,6,8,3])

