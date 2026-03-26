#Check Even/Odd Using Bitwise Operator
"""
8 = 1000
1 = 0001
------------
&   0000
"""
def even_odd(n):                #bitwise operator works as AND operator & converts int to binary
    if n & 1 == 0:              
        return "even"           #binary code of even numbers end always in 0
    else:
        return "odd"
print(even_odd(2))
print(even_odd(25))