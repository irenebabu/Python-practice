#find the maximum product pair

def max_product(numbers):
    max_product = int()
    pairs = ()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            product = numbers[i]*numbers[j]

            if product > max_product:
                max_product = product
                pairs = (numbers[i],numbers[j])

    return pairs

print(max_product((4,5,6,2,3,7)))
