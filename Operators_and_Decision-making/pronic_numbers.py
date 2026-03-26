"""
check whether given number is pronic or not.
A pronic number is a number 
which is the product of two consecutive integers,
eg : 6 = 2x3 6 is pronic, 20 (4*5)

"""

def is_pronic(n):
    for i in range(0,n):
        if n == i*(i+1):
            return True
    return False

print(is_pronic(6))
print(is_pronic(16))