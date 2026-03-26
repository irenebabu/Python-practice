#convert an integer into list and reverse the order

def number_to_reversed_list(n):
    lst = []
    length = len(str(n))
    while n!=0:
        last_digit = n%10
        lst.append(last_digit)
        n = n//10
    return lst

print(number_to_reversed_list(6789))