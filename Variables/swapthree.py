'''
1) 🔄 Cyclic Swap of Three Variables (no extra variable)

Rotate values:
👉 Example

a = 10, b = 20, c = 30  
→ a = 30, b = 10, c = 20
use arithmetic cycling
Constraints: No temp variable, no tuple unpacking.
'''

def swap_three(a, b, c):      #a = 1, b= 2,c = 3

    a = a + b + c               #a = 6

    b = a - (b + c)   # total = a   #b = 6 - (2+3) = 1 ( new b)
    c = a - (b + c)   # new b       #c = 6 - (1+3) = 2 (new c)
    a = a - (b + c)   # new b,c     #a = 6 - (1+2) = 3 (new a)

    print(f"a = {a}  b = {b}  c = {c}")

swap_three(1,2,3)