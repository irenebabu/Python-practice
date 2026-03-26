#convert from celsius to Fahrenheit formula = c * 9/5  + 32  = F

def convert(celsius_list):
    fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_list))
    return fahrenheit

print(convert([37,40,20]))