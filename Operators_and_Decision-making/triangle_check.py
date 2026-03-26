"""
Valid Triangle Check

Given 3 sides:

👉 Check if they can form a triangle

( sum of any two sides > third) follow all three conditions

"""
def triangle(n1,n2,n3):
    
    if (n1 + n2)>n3 and (n1 + n3)>n2 and (n2 + n3)>n1:
        return True
    else:
        return False

print(triangle(1,2,3))
print(triangle(2,2,3))

