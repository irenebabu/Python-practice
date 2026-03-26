#check whether the input contains all digits 0–9 at least once. (Pandigital number or not)

def is_number_pandigital(num):
    num = str(num)
    pandigits = "1234567890"
    for i in pandigits:
        if i not in num:
            return False
    return True     

print(is_number_pandigital(56))
print(is_number_pandigital(12354056789))