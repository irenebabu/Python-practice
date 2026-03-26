#Display the prime factors of a given number(except 1)

def prime_factor(num):
    
    i = 2
    while i<=num:
        if num%i==0:
            print(i,",",end=" ")
            num = num//i
        else:
            i+=1
prime_factor(60)