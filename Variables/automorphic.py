"""
Automorphic/circular Number Check

Number whose square ends with the same digits.
👉 Example

76 → 76² = 5776 → ends with 76
"""

def automorphic(num):

    square = num**2
    if square%(10**len(str(num))) == num:
        print(num,"is an automorphic number.","The square of the number is",square)
    else:
        print(num,"is not Automorphic")

automorphic(76)
automorphic(11)
automorphic(5)
