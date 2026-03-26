#show mutability in list with an example
def add_item(lst):
    lst.append(100)


nums = [1, 2, 3]
add_item(nums)
print(nums)