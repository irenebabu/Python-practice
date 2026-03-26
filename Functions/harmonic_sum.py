#return sum of harmonic series rounded off to two decimals. if n = 5
#1 + 1/2 +1/3 + 1/4 + 1/5 = 2.28

def harmonic(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + 1/i
    return round(sum,2)

print(harmonic(5))