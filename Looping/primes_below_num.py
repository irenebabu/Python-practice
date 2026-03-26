#print prime nums below given number
def primes_below(n):
    primes = []
    for num1 in range(2, n):
        for num2 in range(2, num1):
            
            if num1 % num2 == 0:
                break

        else:
                primes.append(num1)

    return primes

print(primes_below(10))

