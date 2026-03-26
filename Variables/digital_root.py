"""
2) 🔢 Digital Root Calculator

Keep summing digits until a single digit remains.

👉 Example

9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2
Output: 2
"""

def digital_root(num):
    while len(str(num))>1:
        total = 0
        while num>0:
            last = num%10
            total = total + last
            num = num//10
        num = total
    print(num)

digital_root(456)
