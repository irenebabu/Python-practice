#Create a program to find the sum of the square root of two numbers using a lambda function.
def squares(n1,n2):
    compute = lambda n1,n2:(n1**0.5)+ (n2**0.5)
    return compute(n1, n2) 


n1 = int(input("n1: "))
n2 = int(input("n2: "))

print(squares(n1,n2))