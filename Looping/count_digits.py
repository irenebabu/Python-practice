def count_digits(n):
    count = 0
    while n!=0:
        last = n%10
        count+=1
        n = n//10
    return count


print(count_digits(456))
print(count_digits(4560235))