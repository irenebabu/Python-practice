"""
Given an integer, 
print "Weird" or "Not Weird" based on these rules: 
If int is odd, print Weird.
If int is even and in the inclusive range of 2 to 5, print Not Weird.
If int is even and in the inclusive range of 6 to 20, print Weird.
If int is even and greater than 20, print Not Weird.
 """

def is_weird(n):
    if n % 2!=0 or 6 <= n <= 20:
        return "Weird"
    return "Not Weird"

print(is_weird(16))
print(is_weird(4))
print(is_weird(24))

