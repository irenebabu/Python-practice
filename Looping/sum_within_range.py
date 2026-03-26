#sum of digits within inclusive range ;eg:
#  eg : (10-15) 1+0  + 1+1  + 1+2 + 1+3 + 1+4  + 1+5  = 21

def sum_of_digits(start, end):
    
    total = 0   

    for n in range(start, end + 1):
        
        last = n % 10
        first = n // 10   
        
        digit_sum = last + first
        
        total = total + digit_sum

    print(total)

sum_of_digits(21, 23)